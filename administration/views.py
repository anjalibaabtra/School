from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from administration.models import AdminUser, Students

# Create your views here.
def adminlogin(request):
    
    if request.method=='POST':
        uname = request.POST['uname']
        password = request.POST['password']
        user = authenticate(request, username=uname, password=password)
        if user is not None:
            login(request, user)
            return redirect('adminDashboard')
            # return render(request, 'adminDashboard.html')

        else:
            messages.info(request, 'Invalid Username or Password')
            # return redirect('adminLogin')
            return render(request, 'adminLogin.html')
    else:
        # return redirect('adminLogin')
        return render(request, 'adminLogin.html')
    # return render(request, 'adminlogin.html')


def adminLogout(request):
    logout(request)
    return redirect('adminLogin')
    # return render(request, 'Administration/index.html')

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
                username=uname, password=password, is_admin = True)
            user_data.save()
            # return redirect('AdminLogin')
            return render(request, 'adminLogin.html')
    else:
        return render(request, 'adminSignup.html')
    # return render(request, 'adminSignup.html')



def viewactiveStudents(request):
    allstudents = Students.objects.all()
    # act=False
    
    # if Students.objects.get(active=False):
    #     val = 'Inactive'
    # else:
    #     val = 'Active'
    return render(request, 'viewactiveStudents.html', {'students': allstudents})
    # return render(request,'viewactiveStudents.html')


    
def registerStudents(request):
    if request.method == 'POST':
        name = request.POST['name']
        contact = request.POST['contact']
        email = request.POST['email']
        uname = request.POST['uname']
        password = request.POST['password']
        if Students.objects.filter(Username=uname).exists():
            messages.info(request, 'Username already used')
            return render(request, 'registerStudents.html')
        else:
            user_data = AdminUser.objects.create_user(
                username=uname, password=password, is_student = True)
            user_data.save()
            student_data = Students.objects.create(Name = name, Contact = contact, Email = email, Username = uname, Password = password)
            student_data.save()
            return render(request, 'registerStudents.html')
    else:
        return render(request,'registerStudents.html')