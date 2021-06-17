from django.urls import path
from polls import views


urlpatterns = [
    path('api/poll/', views.PollAPIView.as_view(), name="poll_api_view"),
    path('api/poll/<int:id>/', views.PollAPIView.as_view(), name="poll_api_view_id"),
    path('api/question/', views.QuestionAPIView.as_view(), name="question_api_view"),
    path('api/question/<int:id>/', views.QuestionAPIView.as_view(), name="question_api_view_id"),

    path('user/poll/<int:id>/', views.PollUserView.as_view(), name="PollUserView_id"),
    path('user/poll/', views.PollUserView.as_view(), name="PollUserView"),
    path('user/vote/<int:id>/', views.PollVoting, name="vote"),
    # path('user/question/<int:id>/', views.PollUserView.as_view(), name="PollUserView"),
]
