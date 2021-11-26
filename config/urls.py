from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from survey.viewsets.survey_viewset import SurveyViewSet

router = routers.DefaultRouter()
router.register(r'surveys', SurveyViewSet, basename='surveys')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
