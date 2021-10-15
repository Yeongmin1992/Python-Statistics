from django.urls import path

from . import views

# 어플리케이션 이름공간 설정 -> 비슷한 역할을 하는 url을 그룹으로 묶어주는 역할
app_name = 'polls'

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),

    
    # path('test/', views.test, name='index'),
]