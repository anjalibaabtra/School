from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from administration.models import AdminUser

# Create your views here.
def adminlogin(request):
    
    if request.method=='POST':
        uname = request.POST['uname']
        password = request.POST['password']
        user = authenticate(request, username=uname, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'adminDashboard.html')

        else:
            messages.info(request, 'Invalid Username or Password')
            return render(request, 'adminLogin.html')
    else:
        return render(request, 'adminLogin.html')
    # return render(request, 'adminlogin.html')


def adminDash(request):
    return render(request, 'adminDashboard.html')

def adminSignup(request):
    if request.method == 'POST':
        uname = request.POST["uname"]
        # email = request.POST["email"]
        password = request.POST["password"]
        if AdminUser.objects.filter(username=uname).exists():
            messages.info(request, 'Username already used')
            # return redirect('signup')
            return render(request, 'adminSignup.html')
        # elif AdminUser.objects.filter(uname=email).exists():
        #     messages.info(request, 'Email already used')
        #     # return redirect('signup')
        #     return render(request, 'adminSignup.html')
        else:
            user_data = AdminUser.objects.create_user(
                username=uname, password=password)
            user_data.save()
            # return redirect('AdminLogin')
            return render(request, 'adminLogin.html')
    else:
        return render(request, 'adminSignup.html')
    # return render(request, 'adminSignup.html')

def viewactiveStudents(request):
    return render(request,'viewactiveStudents.html')
    
def registerStudents(request):
    return render(request,'registerStudents.html')