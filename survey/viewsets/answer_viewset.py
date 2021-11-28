from rest_framework import mixins, viewsets
from django_filters import rest_framework as drf_filters
from django_filters.rest_framework import DjangoFilterBackend
from survey.models.answer import Answer
from survey.serializers.answer_serializer import AnswerSerializer


class AnswerFilter(drf_filters.FilterSet):
    user_id = drf_filters.NumberFilter(field_name="user")


class AnswerViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AnswerFilter
