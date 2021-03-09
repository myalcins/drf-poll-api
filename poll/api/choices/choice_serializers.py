from rest_framework import serializers
from poll.models import Choice


class ChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Choice
        fields = ('choice_text', 'question', 'voted')
        read_only_fields = ('id', 'voted')
    
    def validate(self, attrs):
        question = attrs['question']
        if question.owner != self.context['request'].user:
            raise serializers.ValidationError("You have not permission for this process.") 