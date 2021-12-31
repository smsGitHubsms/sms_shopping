from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
# Create your views here.
from sms_app.models import cycle
def func(request):
    obj = cycle.objects.all()
    return render(request,"index.html",{'result':obj})

def register(request):
    if request.method=="POST":
        Uname = request.POST['UserName']
        fname = request.POST['FirstName']
        lname = request.POST['LastName']
        mail = request.POST['Email']
        pswd1 = request.POST['Password1']
        pswd2 = request.POST['Password2']

        if pswd1==pswd2:
            if User.objects.filter(username=Uname).exists():
                messages.info(request,"UserName already Taken")
                return redirect('register')
            elif User.objects.filter(email=mail).exists():
                messages.info(request,"Email already Taken")
                return redirect('register')
            user = User.objects.create_user(username=Uname,first_name=fname,last_name=lname,email=mail,password=pswd1)
            # Red color "username" is the field of auth user, White color is fetching value from form
            user.save();
        else:
            messages.info(request, "Password not matched")
            return redirect('register')
        return redirect('/')
    else:
        return render(request,"registration.html")

def login(request):
    if request.method=="POST":
        UnamE = request.POST['UsernamE']
        PswD = request.POST['PassworD']
        UseR=auth.authenticate(username=UnamE,password=PswD)
        if UseR is not None:
            auth.login(request,UseR)
            return redirect('/')
        else:
            messages.info(request,'invalid username or password')
            return redirect('login')
    else:
        return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def search(request):
    query=None
    srch=None
    if 'q' in request.GET:
        query = request.GET.get('q')
        srch = cycle.objects.all().filter(Q(name__contains=query)|Q(desc__contains=query))

    return render(request, "search.html",{'sr':srch})

def rocyc(request):
    abcd = cycle.objects.filter(Q(type__contains='Road'))
    return render(request, "filter.html", {'aaa': abcd})

def mtcyc(request):
    abcd = cycle.objects.filter(Q(name__contains='MTB'))
    return render(request, "filter.html", {'aaa': abcd})

def focyc(request):
    abcd = cycle.objects.filter(Q(name__contains='Foldable'))
    return render(request, "filter.html", {'aaa': abcd})

def home(request):
    return redirect('/')

