from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth.models import User

QUESTION_TYPE_CHOICES = (
    (1, 'Multiple Choice Answer'),
    (2, 'Single Choice Answer'),
    (3, 'Text Answer')
)


class Poll(models.Model):
    """
        Model for storing polls

        name:               poll's name
        desription:         poll's description
        start_date:         poll's startig time
        end_date:           poll's ending time
    """
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)

    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.name


class Question(models.Model):
    """
        Model for storing questions for a poll

        q_text : question text
        q_type : question type where
                1 - MultipleChoiceAnswer
                2 - SingleChoiceAnswer
                3 - TextAnswer
    """
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='questions', default=None)
    q_text = models.CharField(max_length=200, name="question text")
    q_type = models.IntegerField(choices=QUESTION_TYPE_CHOICES, name="question type")

    def __str__(self):
        return self.__getattribute__("question text")


class BaseMultipleChoiceAnswer(models.Model):
    """
        Model for possible answers for a question with multiple choices
    """

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = ArrayField(
        models.CharField(max_length=100, blank=True)
    )


class BaseSingleChoiceAnswer(models.Model):
    """
        Model for possible answers for a question with a single choice
    """

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=100, null=False)


class BaseTextAnswer(models.Model):
    """
        Model for a text answer to a question with a text response
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=5000, null=False)


class Answer(models.Model):
    """
        Model that stores single answer to a question from a user.

        answer should be an ArrayField
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=5000, null=False)
