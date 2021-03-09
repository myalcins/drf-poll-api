from django.core.exceptions import ValidationError
from django.db import models
from rest_framework import serializers
from poll.models import Choice, Question
from django.db import transaction


class ChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Choice
        fields = ('choice_text', 'voted')
        read_only_fields = ('id', 'question', 'voted')


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
                # 'is_published',
                'created_at',
                'owner')
        read_only_fields = ('pk',
                            'is_published',
                            'created_at',
                            'owner')

    def validate_choices(self, value):
        if len(value) == 0:
            raise serializers.ValidationError("Choices fields is required.")
        if len(value) == 1:
            raise serializers.ValidationError("The question must have at least two choices.")
        return value

    def create(self, validated_data):
        choices_data = validated_data.pop('choices')
        question = Question.objects.create(**validated_data)
        for choice in choices_data:
            Choice.objects.create(question=question, **choice)

        return question
