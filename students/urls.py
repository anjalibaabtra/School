from students import views
from django.urls import path


urlpatterns = [
        path('studentslogin', views.studentslogin, name = 'studentslogin'),
        path('studentDashboard', views.studentDashboard, name = 'studentDashboard'),
        path('updProf/<int:StudentId>', views.updProf, name = 'updProf'),
        path('updateProfile', views.updateProfile, name = 'updateProfile'),
        path('logout', views.studentLogout, name='logout'),
]