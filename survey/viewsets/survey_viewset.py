from rest_framework import mixins, viewsets
from rest_framework.response import Response
from survey.models.survey import Survey
from survey.serializers.survey_serializer import SurveySerializer
import datetime

class SurveyViewSet(mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer

    def list(self, request, *args, **kwargs):
        date = datetime.datetime.now()

        queryset = self.filter_queryset(
            self.get_queryset().filter(start_date__lte=date, end_date__gte=date))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data) 
