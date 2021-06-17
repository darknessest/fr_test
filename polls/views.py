from rest_framework import status, generics, mixins
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.generics import get_object_or_404
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import date
from polls.serializers import *
from rest_framework import status
from polls.models import BaseTextAnswer, BaseSingleChoiceAnswer, BaseMultipleChoiceAnswer
from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from itertools import chain


class PollAPIView(generics.GenericAPIView,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin, mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
    serializer_class = PollSerializer
    queryset = Poll.objects.all()
    lookup_field = 'id'
    permission_classes = [IsAdminUser]

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


class QuestionAPIView(generics.GenericAPIView,
                      mixins.ListModelMixin,
                      mixins.CreateModelMixin, mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    lookup_field = 'id'
    permission_classes = [IsAdminUser]

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


class PollUserView(APIView):
    authentication_classes = [SessionAuthentication,
                              TokenAuthentication,
                              BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        """
        Authenthicated user can get only a list of active polls

        :param request:
        :return:
        """
        today = date.today()
        polls = []
        if id:
            polls = [get_object_or_404(Poll, pk=id)]
        else:
            polls = Poll.objects.all().filter(start_date__lt=today, end_date__gt=today)
        serializer = PollSerializer(polls, many=True)
        return Response(serializer.data)


@api_view(('GET', 'POST'))
@renderer_classes([JSONRenderer, ])
def PollVoting(request, id):
    """
    This functions handles poll voting by poll id.

    :param request:
    :param id:      poll id
    :return:
    """
    if request.user.is_authenticated:
        if request.method == 'GET':
            """
                Returns whole information about 
            """

            resp = {
                "poll_id": id,
                "questions": []
            }

            poll = Poll.objects.get(pk=id)
            if poll:
                questions = Question.objects.filter(poll_id=id)
                if len(questions) > 0:
                    for q in questions:
                        multi_ans_data = BaseMultipleChoiceAnswer.objects.filter(question_id=q.id).values_list('answer')
                        single_ans_data = BaseSingleChoiceAnswer.objects.filter(question_id=q.id).values_list('answer')
                        text_ans_data = BaseTextAnswer.objects.filter(question_id=q.id).values_list('answer')
                        resp['questions'].append({
                            "id": str(q.id),
                            "text": str(q),
                            "answers": list(chain(*text_ans_data, *multi_ans_data, *single_ans_data))
                        }
                        )
                    return Response(resp, status=status.HTTP_200_OK)
                return Response(resp, status=status.HTTP_204_NO_CONTENT)
            return Response(resp, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'POST':
            """
            Expected json:
                {
                    "user_id": ,
                    "question_id": ,
                    "answers": [""]
                }
            """

            answer_serializer = AnswerSerializer(data=request.data)
            print(request.data)
            if answer_serializer.is_valid():
                ans = Answer.objects.create(
                    user=User.objects.get(pk=request.data['user_id']),
                    question=Question.objects.get(pk=request.data['question_id']),
                    answer=request.data['answers']
                )
                ans.save()
                return Response(status=status.HTTP_201_CREATED)
            return Response(answer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response({}, status.HTTP_401_UNAUTHORIZED)
