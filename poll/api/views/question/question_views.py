from rest_framework import serializers
from poll.models import Question
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.mixins import DestroyModelMixin
from .question_serializers import QuestionSerializer
from rest_framework.permissions import IsAuthenticated


class QuestionCreateAPIViews(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionListAPIView(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionDetailAPIView(RetrieveAPIView, DestroyModelMixin):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    lookup_field = 'slug'

    def delete(self, request, *args, **kwargs):
        question = self.get_object()
        if request.user == question.user:
            return self.destroy(request, *args, **kwargs)
        raise serializers.ValidationError("Hop hemşerim nereye!")
