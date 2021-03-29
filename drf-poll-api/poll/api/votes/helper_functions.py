from poll.models import Vote
from django.db.models import Q


def is_voted(user, question):
    if  Vote.objects.filter(Q(owner=user) & Q(question=question)):
        return True 
