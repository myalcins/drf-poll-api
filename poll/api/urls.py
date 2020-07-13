from django.urls import path
from poll.api.views.question.question_views import QuestionCreateAPIViews, QuestionListAPIView, QuestionDetailAPIView
from poll.api.views.vote.vote_views import VoteAPIView, VoteUpdateAPIView, VoteListAPIView


urlpatterns = [
    path('question/', QuestionCreateAPIViews.as_view(), name='question-create'),
    path('question/list/', QuestionListAPIView.as_view(), name='question-list'),
    path('question/<slug>', QuestionDetailAPIView.as_view(), name='question-detail'),
    path('vote/', VoteAPIView.as_view(), name='question-vote'),
    path('vote/edit/<int:pk>', VoteUpdateAPIView.as_view(), name='vote-edit'),
    path('vote/list', VoteListAPIView.as_view(), name='vote-list')
]
