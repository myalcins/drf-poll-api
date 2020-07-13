from rest_framework import serializers
from poll.models import Choice


class ChoiceSerializers(serializers.ModelSerializer):

    class Meta:
        model = Choice
        fields = ['choice_text', 'voted']

    def update(self, instance, validated_data):
        instance.choice_text = validated_data.choice_text
        instance.question = validated_data.question
        instance.voted = validated_data.voted
        instance.save()
        return instance
