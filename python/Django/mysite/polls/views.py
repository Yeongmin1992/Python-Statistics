from django.template import loader
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from .models import Choice, Question

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse


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
    question = get_object_or_404(Question, pk=question_id)
    try:
        # question.choice_set은 해당 key를 외래키로 갖고 있는 choice_set을 의미, pk는 post요청으로 들어온 request의 'choice' 값
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        # post 요청이 왔을 때 대게 reverse함수를 사용하여 response를 함
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


# def test(request):
#    return HttpResponse("Hello, world. You're at the test index.")