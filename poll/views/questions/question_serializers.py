from django.db import models
from rest_framework import serializers
from poll.models import Choice, Question


class ChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Choice
        fields = ('choice_text',
                  'voted')


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)

    class Meta:
        model = Question
        fields = ('pk',
                  'title',
                  'image',
                  'question_text',
                  'description',
                  'choices',
                  'task',
                  'created_at',
                  'user')

    def create(self, validated_data):
        user = self.context['request'].user
        choices_data = validated_data.pop('choices')
        question = Question.objects.create(user=user, **validated_data)
        for choice_data in choices_data:
            Choice.objects.create(question=question, **choice_data)
        return question
