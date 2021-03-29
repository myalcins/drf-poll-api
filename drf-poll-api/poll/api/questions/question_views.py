from rest_framework.response import Response
from poll.api_views import QuestionViewSet
from poll.models import Question
from .question_serializers import QuestionSerializer
from rest_framework import permissions
from .permissions import IsOwner


class QuestionViewSet(QuestionViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    http_method_names = ['head', 'get', 'post', 'delete']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        if self.action == 'destroy':
            permission_classes = (permissions.IsAuthenticated ,IsOwner,)
        else:
            permission_classes = (permissions.IsAuthenticated,)

        return [permission() for permission in permission_classes]