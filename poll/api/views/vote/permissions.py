from rest_framework.permissions import BasePermission
from poll.models import Vote


class VoteisOwner(BasePermission):

    def has_permission(self, request, view):
        user = request.user
        is_owner = Vote.objects.filter(user=user).exists()
        return is_owner

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user
