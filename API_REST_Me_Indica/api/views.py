from rest_framework.response import Response
from rest_framework import status
from rest_framework_mongoengine import viewsets

from .models import LogicQuestion
from .serializer import LogicQuestionSerializer
from ..settings import NUMBER_OF_QUESTION_PER_LEVEL as nqpl
from random import sample

from copy import copy


class LogicQuestionViewSet(viewsets.ModelViewSet):
    lookup_field = "id"
    queryset = LogicQuestion.objects.all()
    serializer_class = LogicQuestionSerializer

    def options(self, request, *args, **kwargs):
        return super(LogicQuestionViewSet, self).options(request, args, kwargs)

    def create(self, request, *args, **kwargs):
        if request.data != {}:
            return super(LogicQuestionViewSet, self).list(request, args, kwargs)

        try:
            list_of_questions = []
            for i in range(0, 7):
                question = list(LogicQuestion.objects.filter(level=i))
                if len(question) == 0:
                    return Response("Problem In Database", status=status.HTTP_404_NOT_FOUND)

                question = sample(question, k=nqpl)
                for j in question:
                    logic_question_data = copy(LogicQuestionSerializer(j).data)
                    del logic_question_data["id"]
                    list_of_questions.append(logic_question_data)

            return Response(list_of_questions, status=status.HTTP_201_CREATED)
        except Exception:
            self.error_message()
