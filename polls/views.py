"""
This is the views.py file
"""
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import Question


def index(request) -> HttpResponse:
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id) -> HttpResponse:
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id) -> HttpResponse:
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id) -> HttpResponse:
    return HttpResponse("You're voting on question %s." % question_id)