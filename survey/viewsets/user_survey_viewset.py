from rest_framework import mixins, viewsets
from django_filters import rest_framework as drf_filters
from django_filters.rest_framework import DjangoFilterBackend
from survey.models.user_survey import UserSurvey
from survey.serializers.user_survey_serializer import UserSurveySerializer


class UserSurveyFilter(drf_filters.FilterSet):
    user_id = drf_filters.NumberFilter(field_name="user")


class UserSurveyViewSet(mixins.CreateModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    queryset = UserSurvey.objects.all()
    serializer_class = UserSurveySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserSurveyFilter
