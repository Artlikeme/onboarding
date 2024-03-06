from django.contrib import admin
from django.urls import path

from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.survey_list, name='survey_list'),
    path('survey/<int:survey_id>/', views.take_survey, name='take_survey')
]
