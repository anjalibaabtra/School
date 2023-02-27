from students import views
from django.urls import path


urlpatterns = [
        path('studentslogin', views.studentslogin, name = 'studentslogin')
]