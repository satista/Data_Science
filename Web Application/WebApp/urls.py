
from django.contrib import admin
from django.urls import path

from trivia_quiz.views import trivia_quiz_list_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("quizzes/",trivia_quiz_list_view)
]
