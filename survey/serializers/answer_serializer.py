from survey.models.answer import Answer
from rest_framework import serializers
from survey.serializers.question_serializer import QuestionSerializer


class AnswerSerializer(serializers.ModelSerializer):
    
    question_data = QuestionSerializer(
        source="question", read_only = True)
       
    class Meta:
        model = Answer
        fields = '__all__'