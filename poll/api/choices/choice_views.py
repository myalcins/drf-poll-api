from django.db import models
from poll.api_views import ChoiceViewSet
from poll.models import Choice
from poll.api.choices.choice_serializers import ChoiceSerializer


class ChoiceViewSet(ChoiceViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

    def get_queryset(self):
        return self.queryset.filter(question__owner=self.request.user)