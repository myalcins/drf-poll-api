from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status
from model_bakery import baker
from django.conf import settings
from poll.models import Choice, Question


def populate_question_url(question=None):
    if question is None:
        return reverse("poll:question-list")
    return reverse("poll:question-detail", kwargs={"pk": question.id})


class QuestionTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = baker.make(settings.AUTH_USER_MODEL)
        self.user2 = baker.make(settings.AUTH_USER_MODEL)
        self.question = baker.make(Question, title="Created by baker.", owner=self.user)

    def test_get_questions_unauthenticated(self):
        url = populate_question_url()
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_question_without_choices(self):
        question = {"title": "Test Question",
                    "question_text": "Can I create a question?",
                    "description": "Hello, I am testing.",
                    "task": False,
                    "choices": []}
        url = populate_question_url()
        self.client.force_authenticate(self.user)
        response = self.client.post(url, data=question, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_question_with_one_choices(self):
        question = {"title": "Test Question",
                    "question_text": "Can I create a question?",
                    "description": "Hello, I am testing.",
                    "task": False,
                    "choices": [{'choice_text': "Choice 1"},]}
        url = populate_question_url()
        self.client.force_authenticate(self.user)
        response = self.client.post(url, data=question, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
 
    def test_create_question(self):
        question = {"title": "Test Question",
                    "question_text": "Can I create a question?",
                    "description": "Hello, I am testing.",
                    "task": False,
                    'choices': [
                        {'choice_text': "Choice 1"},
                        {'choice_text': "Choice 2"},
                        {'choice_text': "Choice 3"},]}
        url = populate_question_url()
        self.client.force_authenticate(self.user)
        response = self.client.post(url, data=question, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertFalse(response.data['task'])        

    def test_get_question_list(self):
        url = populate_question_url()
        self.client.force_authenticate(self.user)
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_get_question_detail(self):
        url = populate_question_url(self.question)
        self.client.force_authenticate(self.user)
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Created by baker.")

    def test_update_question(self):
        data = { "task": False }
        url = populate_question_url(self.question)
        self.client.force_authenticate(self.user)
        response = self.client.patch(url, data=data)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_delete_not_owned_question(self):
        url = populate_question_url(self.question)
        self.client.force_authenticate(self.user2)
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_owned_question(self):
        url = populate_question_url(self.question)
        self.client.force_authenticate(self.user)
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

