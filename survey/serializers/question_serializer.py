from survey.models.question import Question
from rest_framework import serializers
from survey.serializers.option_serializer import OptionSerializer
# from survey.serializers.answer_serializer import AnswerSerializer


class QuestionSerializer(serializers.ModelSerializer):
    option_data = OptionSerializer(
        source="options", many=True, required=False, read_only=True)

            
    class Meta:
        model = Question
        fields = '__all__'