from survey.models.answer_option import AnswerOption
from rest_framework import serializers


class AnswerOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerOption
        fields = '__all__'