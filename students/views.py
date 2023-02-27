from django.shortcuts import render

# Create your views here.
def studentslogin(request):
    return render(request, 'studentslogin.html')
