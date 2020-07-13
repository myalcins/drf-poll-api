from rest_framework import serializers
from poll.models import Question, Choice,  Vote
from poll.api.serializers import ChoiceSerializers


class QuestionSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='question-detail', lookup_field='slug')
    user = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = [
            'url',
            'title',
            'image',
            'question_text',
            'user'
        ]

    def get_user(self, obj):
        return obj.user.username


class VoteSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    question = QuestionSerializer()
    choice = serializers.SerializerMethodField()

    class Meta:
        model = Vote
        fields = ['user',
                  'question',
                  'choice']

    def get_user(self, obj):
        return obj.user.username

    def get_choice(self, obj):
        return obj.choice.choice_text

    def validate(self, attrs):
        user = self.context['request'].user
        choice = attrs['choice']
        votes = Vote.objects.filter(user=user)
        for voted in votes:
            if choice == voted.choice:
                raise serializers.ValidationError(
                    "Yanıtınız zaten mevcut. İşlem için cevabınızda lütfen değişiklik yapınız.")
        return attrs

    def create(self, validated_data):
        user = self.context['request'].user
        choice = validated_data['choice']
        question = choice.question
        votes = Vote.objects.filter(user=user)
        for voted in votes:
            if choice.question == voted.question:
                raise serializers.ValidationError(
                    "Bu soruyu zaten yanıtladınız.")
        voted_choice = Choice.objects.get(id=choice.id)
        voted_choice.voted += 1
        ChoiceSerializers.update(ChoiceSerializers, voted_choice, voted_choice)
        return Vote.objects.create(user=user, question=question, choice=choice)

    def update(self, instance, validated_data):
        user = self.context['request'].user
        votes = Vote.objects.filter(user=user)
        choice = instance.choice
        for voted in votes:
            if choice.question == voted.question:
                choice.voted = choice.voted - 1
                ChoiceSerializers.update(ChoiceSerializers, choice, choice)
        instance.user = user
        instance.question = validated_data.get('question', instance.question)
        instance.choice = validated_data.get('choice', instance.choice)
        instance.save()
        choice = validated_data['choice']
        choice.voted += 1
        ChoiceSerializers.update(ChoiceSerializers, choice, choice)
        return instance
