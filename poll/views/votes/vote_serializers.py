from django.db import models
from rest_framework import serializers
from poll.models import Vote


class VoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vote
        fields = ('user',
                  'question',
                  'chosen')
        read_only_fields = ('user',
                            'question')

    def create(self, validated_data):
        choice = validated_data['chosen']
        vote = Vote.objects.create(user=self.context['request'].user,
                                   chosen=choice,
                                   question=choice.question)
        vote.save()
        return vote

    def update(self, instance, validated_data):
        instance.chosen = validated_data.get('chosen', instance.chosen)
        instance.save(update_fields=validated_data.keys())
        return instance
