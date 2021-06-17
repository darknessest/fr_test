from django.contrib.postgres.fields import ArrayField
from django.db import models

QUESTION_TYPE_CHOICES = (
    (1, 'Multiple Choice Answer'),
    (2, 'Single Choice Answer'),
    (3, 'Text Answer')
)


class Poll(models.Model):
    """
        name:               poll's name
        desription:         poll's description
        start_date:         poll's startig time
        end_date:           poll's ending time

        creation_timestamp: automatically created timestamp, might be usefull for admins
    """
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)

    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    # creation_timestamp = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.name


class Question(models.Model):
    """
        Атрибуты вопросов: текст вопроса, тип вопроса (ответ текстом
        , ответ с выбором одного варианта, ответ с выбором нескольких вариантов)

        q_text : question text
        q_type : question type where
                1 - MultipleChoiceAnswer
                2 - SingleChoiceAnswer
                3 - TextAnswer
    """
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, default=None)
    q_text = models.CharField(max_length=200, name="question text")
    q_type = models.IntegerField(choices=QUESTION_TYPE_CHOICES, name="question type")

    def __str__(self):
        return self.q_text


class MultipleChoiceAnswer(models.Model):
    """

    """

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=100, null=False)
    answer = ArrayField(
        models.CharField(max_length=100, blank=True)
    )


class SingleChoiceAnswer(models.Model):
    """
        question:
        answer:
    """

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=100, null=False)
    # choice = models.BooleanField(null=False)


class TextAnswer(models.Model):
    """

    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField(null=False)

# class User(models.Model):
#     username = models
