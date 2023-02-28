from administration import views
from django.urls import path


urlpatterns = [
        path('adminlogin', views.adminlogin, name = 'adminLogin'),
        path('adminSignup', views.adminSignup, name = 'adminSignup'),
        path('adminDashboard', views.adminDash, name = 'adminDashboard'),
        path('registerStudents', views.registerStudents, name = 'registerStudents'),
        path('viewactiveStudents', views.viewactiveStudents, name = 'viewactiveStudents'),
        path('logout', views.adminLogout, name='logout'),
]