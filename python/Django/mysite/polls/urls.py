from django.urls import path

from . import views

urlpatterns = [
    # polls 뒤에 빈칸 ''이면 views.index를 보여줘라
    path('', views.index, name='index'),
    # path('test/', views.test, name='index'),
]