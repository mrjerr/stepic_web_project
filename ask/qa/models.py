from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class QuestionManager(models.Manager):
        def new(self):
            return Question.objects.order_by('-added_at')[:10]

        def popular(self):
            return Question.objects.order_by('-rating')


class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=200)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField()
    author = models.ForeignKey(User,  related_name='question_author')
    likes = models.ManyToManyField(User,  related_name='question_likes')


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User,  related_name='ansewr_author')
