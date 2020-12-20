from django.urls import path, include
from poll.api.views.question.question_views import QuestionCreateAPIViews, QuestionListAPIView, QuestionDetailAPIView
from poll.api.views.vote.vote_views import VoteAPIView, VoteUpdateAPIView, VoteListAPIView

from rest_framework import routers
from .api_views import QuestionViewSet, ChoiceViewSet, VoteViewSet
from poll.views.questions.question_views import QuestionViewSet


router = routers.SimpleRouter()
router.register(r'question', QuestionViewSet)
router.register(r'choice', ChoiceViewSet)
router.register(r'vote', VoteViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('question/', QuestionCreateAPIViews.as_view(), name='question-create'),
    path('question/list/', QuestionListAPIView.as_view(), name='question-list'),
    path('question/<slug>', QuestionDetailAPIView.as_view(), name='question-detail'),
    path('vote/', VoteAPIView.as_view(), name='question-vote'),
    path('vote/edit/<int:pk>', VoteUpdateAPIView.as_view(), name='vote-edit'),
    path('vote/list', VoteListAPIView.as_view(), name='vote-list')
]
