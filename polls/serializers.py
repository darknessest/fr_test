# from django.contrib.auth.models import User, Group
from polls.models import Poll, Question
from rest_framework import serializers


class PollSerializer(serializers.ModelSerializer):
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        return instance

    class Meta:
        model = Poll
        fields = ['name', 'description', 'start_date', 'end_date']


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'poll', 'question text', 'question type']
