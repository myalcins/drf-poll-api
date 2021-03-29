from poll.api_views import VoteViewSet
from .vote_serializers import VoteSerializer
from poll.models import Vote


class VoteViewSet(VoteViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)