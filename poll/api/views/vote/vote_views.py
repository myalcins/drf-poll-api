from poll.api.serializers import ChoiceSerializers
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.mixins import DestroyModelMixin
from poll.models import Vote
from .vote_serializers import VoteSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import VoteisOwner


class VoteAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer


class VoteUpdateAPIView(UpdateAPIView, RetrieveAPIView, DestroyModelMixin):
    permission_classes = [IsAuthenticated, VoteisOwner]
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    lookup_field = 'pk'

    def delete(self, request, *args, **kwargs):
        vote = self.get_object()
        choice = vote.choice
        choice.voted = choice.voted - 1
        ChoiceSerializers.update(ChoiceSerializers, choice, choice)
        return self.destroy(request, *args, **kwargs)


class VoteListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated, VoteisOwner]
    serializer_class = VoteSerializer

    def get_queryset(self):
        return Vote.objects.filter(user=self.request.user)
