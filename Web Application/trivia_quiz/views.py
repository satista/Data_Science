from django.shortcuts import render
from .models import trivia_quiz

# Create your views here.

#CRUD - create retrieve update delete

#List all the trivia quiz

def trivia_quiz_list_view(request):
    trivia_quiz_obj =  trivia_quiz.objects.all()
    content = {
        "trivia_quiz_obj": trivia_quiz_obj
    }
    return render(request, "quizzes/index.html", context=content)