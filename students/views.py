from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from administration.models import AdminUser, Students


# Create your views here.
def studentslogin(request):
    if request.method=='POST':
        uname = request.POST['uname']
        password = request.POST['password']
        user = authenticate(request, username=uname, password=password)
        if user is not None and user.is_student:
            login(request, user)
            # return render(request, 'studentDashboard.html')
            return redirect('studentDashboard')
        

        else:
            messages.info(request, 'Invalid Username or Password')
            return render(request, 'studentslogin.html')
    else:
        return render(request, 'studentslogin.html')


def studentLogout(request):
    logout(request)
    return redirect('studentslogin')
    # return render(request, 'Administration/index.html')

def updProf(request, StudentId):
    Students.objects.filter(id=StudentId)
    print(id.is_approved)
    print("Approved")
    allstudents = Students.objects.filter(id=StudentId)
    return render(request, 'updateProfile.html', {'students': allstudents})



def updateProfile(request):
    if request.method == 'POST':
        name = request.POST['name']
        contact = request.POST['contact']
        email = request.POST['email']
        uname = request.POST['uname']
        password = request.POST['password']
        
        # if Students.objects.filter(Username=uname).exists():
        student = Students.objects.get(Name=name)
        stdnt = AdminUser.objects.get(username= student.Username)
        AdminUser.objects.filter(id=stdnt.id).update(username = uname)
        Students.objects.filter(id = student.id).update(Name = name, Contact = contact, Email = email, Username = uname, Password = password)
        
        s = AdminUser.objects.get(id = stdnt.id)
        s.set_password(password)
        
        s.save()
        # usname=request.GET['uname']
        allstudents = Students.objects.filter(Username=uname)
        return render(request, 'updateProfile.html', {'students': allstudents})
    else:
        uname=request.GET['value']
        allstudents = Students.objects.filter(Username=uname)
        return render(request, 'updateProfile.html', {'students': allstudents})



def studentDashboard(request):
    # if request.method == 'POST':
    #     name = request.POST['name']
    #     contact = request.POST['contact']
    #     email = request.POST['email']
    #     uname = request.POST['uname']
    #     password = request.POST['password']
    #     if Students.objects.filter(Username=uname).exists():
    #     #     messages.info(request, 'Username already used')
    #     #     return render(request, 'studentDashboard.html')
    #     # else:
    #         # user_data = AdminUser.objects.create_user(
    #         #     username=uname, password=password, is_student = True)
    #         # user_data.save()
    #         student = Students.objects.get(Name=name)
    #         Students.objects.filter(id = student.id).update(Name = name, Contact = contact, Email = email, Username = uname, Password = password)
    #         # student_data.save()
    #         return render(request, 'studentDashboard.html')
    # else:

        return render(request,'studentDashboard.html')
    # return render(request, 'studentDashboard.html')