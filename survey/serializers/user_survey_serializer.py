from survey.models.user_survey import UserSurvey
from rest_framework import serializers

from survey.serializers.survey_serializer import SurveySerializer


class UserSurveySerializer(serializers.ModelSerializer):
    survey_data = SurveySerializer(source="survey", read_only=True)

    class Meta:
        model = UserSurvey
        fields = '__all__'
