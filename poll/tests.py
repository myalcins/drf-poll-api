from model_bakery import baker
from rest_framework.test import APIClient, APITestCase
from rest_framework import status


class QuestionTest(APITestCase):

    url = "/api/v1/question/"

    def setUp(self):
        self.user = baker.make(
            'User'
        )

    def test_create_question(self):
        client = APIClient()
        client.force_authenticate(self.user)
        data = {
            'title': "Test",
            'question_text': "Test deneme 1 2 3?",
            'description': "teste dair",
            'user': self.user.pk
        }
        response = client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
