from rest_framework.test import APIClient
from django.test import TestCase, client
from model_bakery import baker
from poll.models import Question, Choice, Vote
from django.conf import settings
from rest_framework import status


class SignalTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = baker.make(settings.AUTH_USER_MODEL)
        self.user2 = baker.make(settings.AUTH_USER_MODEL)
        self.question = baker.make(Question)
        self.choice = baker.make(Choice, question=self.question)
        self.choice2 = baker.make(Choice, question=self.question)
        self.user_vote = Vote.objects.create(chosen=self.choice2, question=self.question, owner=self.user2)
        
    def test_increase_chosen_voted_count(self):
        # it works when created vote objects
        vote = Vote.objects.create(chosen=self.choice, question=self.question, owner=self.user)
        self.assertEqual(Choice.objects.values_list('voted', flat=True).get(pk=self.choice.pk), 1)

    def test_choices_decrease_voted_count(self):
        # it works when vote object deleted
        self.assertEqual(Choice.objects.values_list('voted', flat=True).get(pk=self.choice2.pk), 1)
        self.user_vote.delete()
        self.assertEqual(Choice.objects.values_list('voted', flat=True).get(pk=self.choice2.pk), 0)

    def test_update_vote_object(self):
        # update signals works when send update request to /api/v1/vote/<:id> endpoints
        url = f"/api/v1/vote/{self.user_vote.id}/"
        self.client.force_authenticate(self.user2)
        
        self.assertEqual(Choice.objects.values_list('voted', flat=True).get(pk=self.choice2.pk), 1)
        res = self.client.patch(url, data={"chosen": self.choice.id}, format="json")
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(Choice.objects.values_list('voted', flat=True).get(pk=self.choice2.pk), 0)
        self.assertEqual(Choice.objects.values_list('voted', flat=True).get(pk=self.choice.pk), 1)

