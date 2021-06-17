from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status, generics, mixins
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from polls.models import Poll
from polls.serializers import *


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class PollAPIView(APIView):
    def get(self, request):
        polls = Poll.objects.all()
        serializer = PollSerializer(polls, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PollSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request):
        pass


class QuestionView(generics.GenericAPIView,
                   mixins.ListModelMixin,  # todo: delete
                   mixins.CreateModelMixin, mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)
