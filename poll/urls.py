from poll.models import Question
from django.urls import path, include
from rest_framework import routers
from .api_views import ChoiceViewSet
from poll.views.questions.question_views import QuestionViewSet
from poll.views.votes.vote_views import VoteViewSet


router = routers.SimpleRouter()
router.register(r'question', QuestionViewSet)
router.register(r'choice', ChoiceViewSet)
router.register(r'vote', VoteViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
]
