from poll.api_views import VoteViewSet
from .vote_serializers import VoteSerializer
from poll.models import Vote


class VoteViewSet(VoteViewSet):
    serializer_class = VoteSerializer
    queryset = Vote.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return super().perform_create(serializer)
