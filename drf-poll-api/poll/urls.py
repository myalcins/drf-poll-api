from django.urls import path, include
from rest_framework import routers
from poll.api.questions.question_views import QuestionViewSet
from poll.api.choices.choice_views import ChoiceViewSet
from poll.api.votes.vote_views import VoteViewSet


router = routers.DefaultRouter()
router.register(r'question', QuestionViewSet)
router.register(r'choice', ChoiceViewSet)
router.register(r'vote', VoteViewSet)
app_name = "poll"

urlpatterns = [
    path('v1/', include(router.urls)),
]
