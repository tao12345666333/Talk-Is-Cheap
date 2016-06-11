from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.http import HttpResponse, Http404
from django.template import loader

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list
    }
    # return HttpResponse(template.render(context, request))

    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question dose not exist')
    question = get_object_or_404(Question, pk=question_id)

    # return HttpResponse('now is the detail of %s.' % question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    return HttpResponse('the results of question %s.' % question_id)


def vote(request, question_id):
    return HttpResponse('you vote on question %s.' % question_id)
