from model_bakery import baker
from rest_framework.test import APITestCase
from .service_test import TestMethod
from poll.models import Question, Choice


class QuestionTest(APITestCase, TestMethod):
    def setUp(self):
        self.url = "/api/v1/question/"
        self.question = baker.make('Question')

    def test_create(self):
        data = {
            'title': "Test",
            'question_text': "Test deneme 1 2 3?",
            'description': "teste dair",
            'choices': [
                {"choice_text": "choice test 1"},
                {"choice_text": "choice test 2"},
                {"choice_text": "choice test 3"}
            ]
        }
        r = self.post(data, authenticate=True)
        self.assertEqual(r.status_code, 201)
        
    def test_get(self):
        r = self.get(authenticate=True)
        self.assertEqual(r.status_code, 200)

    def test_get_one(self):
        self.url = self.url + f"{self.question.pk}/"
        r = self.get(authenticate=True)
        self.assertEqual(r.status_code, 200)

    def test_update(self):
        data = data = {
            'title': "Test",
            'question_text': "Test deneme 1 2 3?",
            'description': "teste dair",
            'choices': [
                {"choice_text": "choice test 1"},
                {"choice_text": "choice test 2"},
                {"choice_text": "choice test 3"}
            ]
        }
        self.url = self.url + f"{self.question.pk}/"
        r = self.patch(data, authenticate=True)
        self.assertEqual(r.status_code, 405)