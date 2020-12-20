from rest_framework import viewsets
from poll.api_views import QuestionViewSet
from poll.models import Question
from .question_serializers import QuestionSerializer


class QuestionViewSet(QuestionViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    http_method_names = ['head', 'get', 'post', 'delete']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return super().perform_create(serializer)
