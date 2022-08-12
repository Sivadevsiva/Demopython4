from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['user']
        password=request.POST['pd']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"INVALID CREDENTIALS")
            return redirect('login')
    return render(request,"login.html")

def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        pwd = request.POST['pd']
        cpd = request.POST['cpd']
        if pwd==cpd:
            if User.objects.filter(username=username).exists():
                messages.info(request,"USERNAME TAKEN")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"E-MAIL TAKEN")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,password=pwd,email=email,)
                user.save();
                messages.info(request, "USER REGISTRATION SUCCESSFULL")
                return redirect('login')
        else:
            messages.info(request,"PASSWORD NOT MATCHING")
            return redirect('register')
    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

