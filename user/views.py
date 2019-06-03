from django.shortcuts import render,redirect,HttpResponse
from user.models import UserRegistration
from user.forms import UserRegistrationForm
import datetime as dt
from mislanius_files.mail import mail_sending
from django.contrib.auth.hashers import make_password,check_password


def user_registration(request):
    if request.method == "POST":
        link = make_password(str(request.POST["email"][0:5]) + request.POST["first_name"])
        c_link = link.replace("+", "")
        verify_link = "http://127.0.0.1:8000/link_created/?link="+c_link
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.first_name = request.POST['first_name']
            f.last_name = request.POST['last_name']
            f.email = request.POST['email']
            f.password = make_password(request.POST["password"])
            f.verify_link = c_link
            f.active = 0
            f.save()
            mail_sending(f.first_name, f.email, verify_link)
            return render(request, "user_registration.html", {'success': True})
        else:
            return render(request,"user_registration.html", {'fail': True})
    return render(request, "user_registration.html")



def link_created(request):
    get_link = request.GET['link']
    data = UserRegistration.objects.get(verify_link=get_link)
    link = data.verify_link
    if get_link == link:
        update = UserRegistration(email=data.email, active=1, verify_link="")
        update.save(update_fields=["active","verify_link"])
        return render(request, "login.html")


def login(request):
    if request.method=="POST":
        email = request.POST["email"]
        password = request.POST["password"]
        data = UserRegistration.objects.get(email=email)
        dpassw = data.password
        active = data.active
        if active == 0:
            return render(request, "login.html", {'confirm': True})
        if active == 1:
            if check_password(password, dpassw):
                request.session["authenticated"] = True
                request.session["email"] = email
                update = UserRegistration(email=email,log_in_time=dt.datetime.now())
                update.save(update_fields=["log_in_time"])
                return redirect("/home/")
    return render(request,"login.html")


def home(request):
    return render(request, "home.html")

def change_password(request):
    if request.method=="POST":
        old_passw = request.POST["old_pass"]
        data = UserRegistration.objects.get(email=request.session["email"])
        email = data.email
        old_pass = data.password
        if check_password(old_passw, old_pass):
            new_pass = request.POST["new_pass"]
            confirm_pass = request.POST["confirm_pass"]
            if new_pass == confirm_pass:
                update = UserRegistration(email=email, password=make_password(confirm_pass))
                update.save(update_fields=["password"])
                return redirect('/login/')
            else:
                return render(request,"change_password.html",{'fail':True})
        else:return render(request,"change_password.html",{'error':True})
    return render(request,"change_password.html")



def logout(request):
    get_data = UserRegistration.objects.get()
    email = get_data.email
    request.session['email'] = email
    request.session["authenticated"] = False
    update = UserRegistration(email=email, log_out_time=dt.datetime.now())
    update.save(update_fields=["log_out_time"])
    return redirect("/login/")

