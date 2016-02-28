from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=300)
    published = models.DateTimeField('Publish Date')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=50)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
