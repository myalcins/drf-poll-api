from poll.serializers import QuestionSerializer
from rest_framework import serializers
from poll.models import Choice, Vote
from poll.signals import vote_update
from django.db import transaction
from poll.api.votes.helper_functions import is_voted


class VoteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Vote
        fields = ('id',
                'question',
                'chosen',
                'owner')
        read_only_fields = ('id',
                            'owner',
                            'question')

    def create(self, validated_data):
        question = validated_data['chosen'].question
        # for prevent to creating voting record for second time
        if is_voted(self.context['request'].user, question):
            # To each of the questions, The voting records have one registration of the users.
            raise serializers.ValidationError("Unable to create the voting records for the second time.")
        else:
            vote = Vote.objects.create(question=question,
                                    **validated_data)
        return vote

    @transaction.atomic
    def update(self, instance, validated_data):
        vote_update.send(sender=Vote, instance=instance)
        instance.chosen = validated_data['chosen']
        instance.save(update_fields=["chosen"])
        return instance
