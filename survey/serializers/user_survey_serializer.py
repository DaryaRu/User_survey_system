from survey.models.user_survey import UserSurvey
from rest_framework import serializers


class UserSurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSurvey
        fields = '__all__'