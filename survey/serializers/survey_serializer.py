from survey.models.survey import Survey
from rest_framework import serializers


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = '__all__'