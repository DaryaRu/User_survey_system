from rest_framework import mixins, viewsets
from survey.models.answer import Answer
from survey.serializers.answer_serializer import AnswerSerializer


class AnswerViewSet(mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer