from django.db.models import fields
from .models import Question, Choice, Vote
from rest_framework import serializers


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = '__all__'


class ChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Choice
        fields = '__all__'


class VoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vote
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.chosen = validated_data.get('chosen', instance.chosen)
        instance.save(update_fields=validated_data.keys())
        return instance
