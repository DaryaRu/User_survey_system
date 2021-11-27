from survey.models.survey import Survey
from rest_framework import serializers

from survey.serializers.question_serializer import QuestionSerializer


class SurveySerializer(serializers.ModelSerializer):
    questions_data = QuestionSerializer(
        source="questions", many=True, required=False, read_only=True)

    class Meta:
        model = Survey
        fields = '__all__'
