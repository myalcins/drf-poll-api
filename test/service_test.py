from typing import Dict
from model_bakery import baker


class TestMethod():

    def __init__(self) :
        self.client = None
        self.url = None

    def set_auth(self):
        user = baker.make(
            'User'
        )
        return user

    def post(self, data: Dict, authenticate=False):
        if authenticate:
            self.client.force_authenticate(user=self.set_auth())
        response = self.client.post(self.url, data, format='json')
        return response

    def get(self, data: Dict=None, authenticate=False):
        if authenticate:
            self.client.force_authenticate(user=self.set_auth())set_auth
        response = self.client.get(self.url, data)
        return response

    def patch(self, data: Dict=None, authenticate=False):
        if authenticate:
            self.client.force_authenticate(user=self.set_auth())
        response = self.client.patch(self.url, data=data)
        return response

    def put(self, data:Dict=None, authenticate=False):
        if authenticate:
            self.client.force_authenticate(user=self.set_auth())
        response = self.client.put(self.url, data=data)
        return response

    def delete(self, authenticate=False):
        if  authenticate:
            self.client.force_authenticate(user=self.set_auth())
        response = self.client.delete(self.url)
        return responseset_auth
