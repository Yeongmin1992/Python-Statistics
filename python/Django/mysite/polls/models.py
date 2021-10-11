import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    # 문자형
    question_text = models.CharField(max_length=200)
    # DateTime형
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    # 외래키 -> models.CASCADE는 1번 question이 삭제되면 1번 question을 외래 키로 갖고 있는 선택들도 CASCADE 방식으로 모두 삭제 됨
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # 선택지, 문자열
    choice_text = models.CharField(max_length=200)
    # 투표 수, Integer
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text