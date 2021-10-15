from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from .models import Question


def index(request):
    """
    # pub_date 기준으로 '최근' 5개 뽑기
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # 위에서 뽑은 question list를 ','로 join
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)
    """

    """
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
    """
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # return HttpResponse("You're looking at question %s." % question_id)
    # q = Question.objects.get(pk=question_id)
    q = get_object_or_404(Question, pk=question_id)
    context = {'question': q}
    return render(request, 'polls/detail.html', context)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    # 데이터베이스 수정
    return HttpResponse("You're voting on question %s." % question_id)


# def test(request):
#     return HttpResponse("Hello, world. You're at the test index.")