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
        self.question = baker.make(Question)
        self.choice = baker.make(Choice, question=self.question)
        self.choice2 = baker.make(Choice, question=self.question)
        self.vote = baker.make(Vote, owner=self.user, chosen=self.choice)

    def test_unauthenticate(self):
        url = populate_vote_url()
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_vote_question(self):
        payload = {
            "chosen": self.choice2.id,
        }
        
        url = populate_vote_url()
        self.client.force_authenticate(self.user2)
        response = self.client.post(url, data=payload, format="json")
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

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

    def test_delete_not_owned_vote(self):
        url = populate_vote_url(self.vote)
        self.client.force_authenticate(self.user2)
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_owned_vote(self):
        url = populate_vote_url(self.vote)
        self.client.force_authenticate(self.user)
        response = self.client.delete(url)
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_update_owned_vote(self):
        data = {"chosen": self.choice2.id}
        url = populate_vote_url(self.vote)
        self.client.force_authenticate(self.user)
        response = self.client.patch(url, data=data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['chosen'], self.choice2.id)

    def test_update_not_owned_vote(self):
        data = {"chosen": self.choice2.id}
        url = populate_vote_url(self.vote)
        self.client.force_authenticate(self.user2)
        response = self.client.patch(url, data=data, format="json")

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)