from django.db import models
from rest_framework import serializers
from poll.models import Choice, Question
from django.db import transaction


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
        read_only_fields = ('user',)

    @transaction.atomic
    def create(self, validated_data):
        choices_data = validated_data.pop('choices')
        question = Question.objects.create(**validated_data)
        choice_list_serializer = self.fields['choices']
        for choice_data in choices_data:
            choice_data['question'] = question
        choices = choice_list_serializer.create(choices_data)
        return question

    def update(self, instance, validated_data):
        return instance