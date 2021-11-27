from survey.models.anonymous_user import AnonymousUser
from rest_framework import serializers

class AnonymousUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnonymousUser
        fields = '__all__'