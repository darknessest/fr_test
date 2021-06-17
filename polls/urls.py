from django.urls import path
from polls import views


urlpatterns = [
    path('', views.index, name="index"),
    path('poll/', views.PollAPIView.as_view(), name="poll_api_view"),
    path('question/', views.QuestionView.as_view(), name="question_apiview"),
    path('question/<int:id>/', views.QuestionView.as_view(), name="question_api_view"),
]
