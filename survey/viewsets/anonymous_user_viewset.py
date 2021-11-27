from rest_framework import mixins, viewsets
from survey.models.anonymous_user import AnonymousUser
from survey.serializers.anonymous_user_serializer import AnonymousUserSerializer

class AnonymousUserViewSet(mixins.CreateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    queryset = AnonymousUser.objects.all()
    serializer_class = AnonymousUserSerializer