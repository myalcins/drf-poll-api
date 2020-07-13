from rest_framework import serializers
from poll.api.serializers import ChoiceSerializers
from poll.models import Question, Choice


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializers(many=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='question-detail', lookup_field='slug')
    user = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = [
            'url',
            'image',
            'title',
            'question_text',
            'description',
            'task',
            'user',
            'choices'
        ]

    def get_user(self, obj):
        return obj.user.username

    def create(self, validated_data):
        user = self.context['request'].user
        choices_data = validated_data.pop('choices')
        question = Question.objects.create(user=user, **validated_data)
        for choice_data in choices_data:
            Choice.objects.create(question=question, **choice_data)
        return question
