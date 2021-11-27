from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from survey.viewsets.survey_viewset import SurveyViewSet
from survey.viewsets.anonymous_user_viewset import AnonymousUserViewSet
from survey.viewsets.user_survey_viewset import UserSurveyViewSet
from survey.viewsets.answer_viewset import AnswerViewSet

router = routers.DefaultRouter()
router.register(r'surveys', SurveyViewSet, basename='surveys')
router.register(r'users', AnonymousUserViewSet, basename='users')
router.register(r'user_surveys', UserSurveyViewSet, basename='user_surveys')
router.register(r'answers', AnswerViewSet, basename='answers')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
