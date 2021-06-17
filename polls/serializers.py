# from django.contrib.auth.models import User, Group
from polls.models import Poll, Question, Answer, BaseMultipleChoiceAnswer, BaseSingleChoiceAnswer, BaseTextAnswer
from rest_framework import serializers
from django.contrib.auth.models import User


class PollSerializer(serializers.ModelSerializer):
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        return instance

    class Meta:
        model = Poll
        fields = ['id', 'name', 'description', 'start_date', 'end_date']


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'poll', 'question text', 'question type']


class AnswerSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(read_only=True)
    question_id = serializers.IntegerField(read_only=True)

    answers = serializers.ListField(child=serializers.CharField(max_length=5000, read_only=True, allow_null=False))

    def create(self, validated_data):
        # print(validated_data)
        return Answer.objects.create(
            user=User.objects.get(pk=int(validated_data.get('user_id'))),
            question=Question.objects.get(pk=int(validated_data.get('question_id'))),
            answers=validated_data.get('answers')
        )
