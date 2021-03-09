from django.conf import settings
from django.test import TestCase
from django.urls.base import reverse
from rest_framework.test import APIClient
from poll.models import Question, Choice, Vote
from model_bakery import baker
from test.test_questions import populate_question_url
from rest_framework import status


def populate_vote_url(vote=None):
    if vote is None:
        return reverse("poll:vote-list")
    return reverse("poll:vote-detail", kwargs={"pk": vote.id})


class VoteTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = baker.make(settings.AUTH_USER_MODEL)
        self.user2 = baker.make(settings.AUTH_USER_MODEL)
        self.vote = baker.make(Vote, owner=self.user)

    @staticmethod
    def _create_question_with_choices(title: str, question_text: str, description: str, choices: list):
        question_user = baker.make(settings.AUTH_USER_MODEL)
        client = APIClient()
        payload = {
            "title": title,
            "question_text": question_text,
            "description": description,
            "choices": choices
        }
        url = populate_question_url()
        client.force_authenticate(question_user)
        res = client.post(url, data=payload, format="json")

        return res.data['pk']
    
    def get_choices(self):
        question = self._create_question_with_choices("Test Question", 
                            "How are you today?", "BOOOO", 
                            [{"choice_text": "Good"},
                            {"choice_text": "Bad"},
                            {"choice_text": "Ugly"}])
        choices = Choice.objects.filter(question=question)

        return choices

    def test_unauthenticate(self):
        url = populate_vote_url()
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_vote_question(self):
        choice = self.get_choices().first()
        payload = {
            "chosen": choice.id,
        }
        
        url = populate_vote_url()
        self.client.force_authenticate(self.user)
        response = self.client.post(url, data=payload, format="json")
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Choice.objects.values_list('voted', flat=True).get(pk=choice.pk) ,1)

    def test_list_vote(self):
        url = populate_vote_url()
        self.client.force_authenticate(self.user)
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_not_owned_vote_detail(self):
        url = populate_vote_url(self.vote)
        self.client.force_authenticate(self.user2)
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_owned_vote_detail(self):
        url = populate_vote_url(self.vote)
        self.client.force_authenticate(self.user)
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['owner'], self.user.id)
