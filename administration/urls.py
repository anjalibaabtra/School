from administration import views
from django.urls import path


urlpatterns = [
        path('adminlogin', views.adminlogin, name = 'adminlogin'),
        path('adminSignup', views.adminSignup, name = 'adminSignup'),
        path('adminDash', views.adminDash, name = 'adminDash'),
        path('registerStudents', views.registerStudents, name = 'registerStudents'),
        path('viewactiveStudents', views.viewactiveStudents, name = 'viewactiveStudents')

]