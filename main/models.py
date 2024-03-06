from django.contrib.auth.models import User
from django.db import models


class Survey(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Survey {self.name}"


class Question(models.Model):
    text = models.CharField(max_length=200)

    parent = models.ForeignKey('self',
                               on_delete=models.CASCADE,
                               null=True,
                               blank=True,
                               related_name='children')
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)

    trigger_answer_text = models.CharField(max_length=200,
                                           blank=True,
                                           null=True)

    def __str__(self):
        return f"Question for {self.id}"


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer_text = models.TextField()
