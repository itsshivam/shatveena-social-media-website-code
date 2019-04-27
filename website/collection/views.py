from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail
from random import randint
import math

from .models import user_basic_detail, user_extra_detail, working_detail
from .forms import login_form, signup_form, user_basic_form, user_detail_form, working_form, working_delete


def random_genrator_id(y):
    x1 = randint(65,90)
    x1 = chr(x1)
    x2 = randint(65,90)
    x2 = chr(x2)
    x3 = randint(65,90)
    x3 = chr(x3)
    x4 = randint(0,9)
    x4 = str(x4)
    x5 = randint(0,9)
    x5 = str(x5)
    x6 = randint(97,122)
    x6 = chr(6)
    x7 = randint(97,122)
    x7 = chr(x7)
    x8 = randint(65,90)
    x8 = chr(x8)
    x9 = randint(0,9)
    x9 = str(x9)
    x10 = randint(97,122)
    x10 = chr(x10)
    y = chr(y)
    x = x1+x2+y+x3+x4+x5+x6+x7+x8+x9+x10
    return x



def my_space(request):
    if request.user.is_authenticated():
        username = request.user.get_username()
        query1 = user_extra_detail.objects.get(username = username)
        query2 = working_detail.objects.filter(username = username)
        context = {
            "username" : username,
            "flag" : 1,
            "form1" : user_basic_form(),
            "form2" : working_form(),
            "query1" : query1,
            "query2" : query2,
        }
        if request.method == "POST" and "about_you" in request.POST:
            form = user_basic_form(request.POST or None)
            if form.is_valid():
                date_of_birth = request.POST["date_of_birth"]
                gender = request.POST["gender"]
                website_link = request.POST["website_link"]
                profession = request.POST["profession"]
                relationship_status = request.POST["relationship_status"]
                user_extra_detail.objects.filter(username = username).update(dob = date_of_birth, website_link = website_link, profession = profession, gender = gender, relationship_status = relationship_status)
                return HttpResponseRedirect("/my-space/")
            else:
                return HttpResponseRedirect("/my-space/")
        elif request.method == "POST" and "working_detail" in request.POST:
            form = working_form(request.POST or None)
            if form.is_valid():
                workplace = request.POST["workplace"]
                work_id = random_genrator_id(5)
                working_detail.objects.create(workplace = workplace, work_id = work_id, username = username)
                return HttpResponseRedirect("/my-space/")
            else:
                return HttpResponseRedirect("/my-space/")
        elif request.method == "POST" and "delete_info" in request.POST:
            form = working_delete(request.POST or None)
            if form.is_valid():
                work_id = request.POST["work_id"]
                print work_id
                working_detail.objects.get(work_id = work_id).delete()
                return HttpResponseRedirect("/my-space/")
        else:
            return render(request,"profile/aboutpage.html",context)
    else:
        return HttpResponseRedirect("/")




def account_page(request):
    if request.user.is_authenticated():
        username = request.user.get_username()
        post = get_object_or_404(user_basic_detail, username = username)
        if request.method == "POST":
            form = user_basic_form(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                form = user_basic_form(instance=post)
                context = {
                    'person' : post,
                    'form' : form,
                }
                return render(request,"profile/mainpage.html",context)
        else:
            form = user_basic_form()
            query = User.objects.all()
            context = {
                'person' : post,
                'form' : form,
                'objects' : query
            }
            return render(request,"profile/mainpage.html",context)
    else:
        return HttpResponseRedirect("/")



def professional_page(request):
    if request.user.is_authenticated():
        context = {
            "username" : request.user.get_username(),
            "flag" : 1,
        }
        return render(request,"profile/aboutprof.html",context)
    else:
        return HttpResponseRedirect("/")

def follower_page(request):
    if request.user.is_authenticated():
        context = {
            "username" : request.user.get_username(),
            "flag" : 1,
        }
        return render(request,"profile/follower.html",context)
    else:
        return HttpResponseRedirect("/")

def following_page(request):
    if request.user.is_authenticated():
        context = {
            "username" : request.user.get_username(),
            "flag" : 1,
        }
        return render(request,"profile/following.html",context)
    else:
        return HttpResponseRedirect("/")



def home_page(request):
    if request.user.is_authenticated():
        context = {
            "username" : request.user.get_username(),
            "flag" : 1,
        }
        return render(request, "index.html", context)
    else:
        context ={
        "flag" : 0,
        }
        return render(request, "index.html", context)




def random_genrator():
    x1 = randint(65,90)
    x1 = chr(x1)
    x2 = randint(65,90)
    x2 = chr(x2)
    x3 = randint(65,90)
    x3 = chr(x3)
    x4 = randint(0,9)
    x4 = str(x4)
    x5 = randint(0,9)
    x5 = str(x5)
    x6 = randint(97,122)
    x6 = chr(6)
    x7 = randint(97,122)
    x7 = chr(x7)
    x8 = randint(65,90)
    x8 = chr(x8)
    x9 = randint(0,9)
    x9 = str(x9)
    x10 = randint(97,122)
    x10 = chr(x10)
    x = x1+x2+x3+x4+x5+x6+x7+x8+x9+x10
    return x



# signup page view starts from here

def signup_page(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/")
    else:
        if request.method == "POST":
            form = signup_form(request.POST or None)
            if form.is_valid:
                shatveena1 = request.POST["shatveena1"]
                # ready = request.POST["ready"]
                if shatveena1=="88456732":

                    username = request.POST["username"]
                    email = request.POST["email"]
                    password = request.POST["password"]
                    confirm_password = request.POST["confirm_password"]
                    user1 = False
                    user2 = False
                    user3 = False
                    email1 = False
                    email2 = False
                    pass1 = False
                    pass2 = False
                    pass3 = False

                    if username=="":
                        if email=="":
                            if password=="":
                                user1 = True
                                email1 = True
                                pass1 = True
                            else:
                                if password == confirm_password:
                                    user1 = True
                                    email1 = True
                                else:
                                    user1 = True
                                    email1 = True
                                    pass2 = True
                        else:
                            if User.objects.filter(email = email).exists():
                                if password=="":
                                    user1 = True
                                    pass1 = True
                                    email2 = True
                                else:
                                    if password == confirm_password:
                                        user1 = True
                                        email2 = True
                                    else:
                                        user1 = True
                                        pass2 = True
                                        email2 = True
                            else:
                                if password=="":
                                    user1 = True
                                    pass1 = True
                                else:
                                    if password == confirm_password:
                                        user1 = True
                                    else:
                                        user1 = True
                                        pass2 = True
                    else:
                        if User.objects.filter(username = username).exists():
                            if email=="":
                                if password=="":
                                    user2 = True
                                    email1 = True
                                    pass1 = True
                                else:
                                    if password == confirm_password:
                                        user2  = True
                                        email1 = True
                                    else:
                                        user2 = True
                                        email1 = True
                                        pass2 = True

                            else:
                                if User.objects.filter(email = email).exists():
                                    if password=="":
                                        user2 = True
                                        pass1 = True
                                        email2 = True
                                    else:
                                        if password == confirm_password:
                                            user2 = True
                                            email2 = True
                                        else:
                                            user2 = True
                                            pass2 = True
                                            email2 = True
                                else:
                                    if password=="":
                                        user2 = True
                                        pass1 = True
                                    else:
                                        if password == confirm_password:
                                            user2 = True
                                        else:
                                            user2 = True
                                            pass2 = True

                        else:
                            if email=="":
                                if password=="":
                                    email1 = True
                                    pass1 = True
                                else:
                                    if password == confirm_password:
                                        email1 = True
                                    else:
                                        email1 = True
                                        pass2 = True

                            else:
                                if User.objects.filter(email = email).exists():
                                    if password=="":
                                        pass1 = True
                                        email2 = True
                                    else:
                                        if password == confirm_password:
                                            email2 = True
                                        else:
                                            pass2 = True
                                            email2 = True
                                else:
                                    if password=="":
                                        pass1 = True
                                    else:
                                        if password == confirm_password:
                                            pass2 = False
                                        else:
                                            pass2 = True
                    if user1==False:
                        if len(username)<7:
                            user3 = True
                            user2 = False
                    if pass1 == False:
                        if len(password)<7:
                            pass3 = True
                            pass2 = False


                    if user1==False and user2==False and user3==False and email1==False and email2==False and pass1==False and pass2==False and pass3==False:
                        otp = randint(100000, 999999)
                        print otp
                        otp1 = 9454798442 + otp*47579117054007
                        print otp1
                        subject = "Email verification for Shatveena.com"
                        message="your otp number is %d" %otp
                        # send_mail(subject, message,settings.EMAIL_HOST_USER,[email])
                        context = {
                            "username" : username,
                            "email" : email,
                            "password" : password,
                            "otp1" : otp1,
                        }
                        return render(request,"login/otpcheck.html",context)
                    else:
                        context = {
                            "username" : username,
                            "email" : email,
                            "password" : password,
                            "confirm_password" : confirm_password,
                            "user1" : user1,
                            "user2" : user2,
                            "user3" : user3,
                            "email1" : email1,
                            "email2" : email2,
                            "pass1" : pass1,
                            "pass2" : pass2,
                            "pass3" : pass3,
                        }
                        return render(request,"login/signup.html",context)

                elif shatveena1=="67862901":
                    username = request.POST["shatveena2"]
                    email = request.POST["shatveena3"]
                    password = request.POST["shatveena4"]
                    otp = request.POST["shatveena5"]
                    otp = int(otp)
                    print otp
                    otp1 = ( otp - 9454798442 ) / 47579117054007
                    print otp1
                    otp1 = str(otp1)
                    check = request.POST["otp"]
                    print check
                    if otp1==check:
                        user = User.objects.create_user(username, email, password)
                        user.save()
                        login(request,user)
                        y = random_genrator()
                        user_id = y
                        print user_id
                        query1 = user_basic_detail(username = username, user_id = user_id)
                        query2 = user_extra_detail(username = username, user_id = user_id)
                        query1.save()
                        query2.save()
                        return HttpResponseRedirect("/")
                    else:
                        return render(request,"login/wrong_otp.html",{})

                elif shatveena1=="44987652":
                    username = request.POST["shatveena2"]
                    email = request.POST["shatveena3"]
                    password = request.POST["shatveena4"]
                    otp = randint(100000, 999999)
                    print otp
                    otp1 = 9454798442 + otp*47579117054007
                    print otp1
                    subject = "Email verification for Shatveena.com"
                    message="your otp number is %d" %otp
                    # send_mail(subject, message,settings.EMAIL_HOST_USER,[email])
                    context = {
                        "username" : username,
                        "email" : email,
                        "password" : password,
                        "otp1" : otp1,
                        "message" : "OTP is sent again on your mail ID"
                    }
                    return render(request,"login/otpcheck.html",context)

        else:
            form = signup_form()
            return render(request,"login/signup.html",{'form' : form})

# signup page view ends here

# login page view starts here

def login_page(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/")
    else:
        if request.method == "POST":
            form = login_form(request.POST)
            if form.is_valid:
                page = request.POST["shatveena1"]
                if page=="570386":
                    username = request.POST["username"]
                    password = request.POST["password"]
                    user = authenticate(username = username, password = password)
                    user1 = False
                    pass1 = False
                    if user is not None:
                        login(request,user)
                        return HttpResponseRedirect("/")
                    else:
                        if username == "" and password == "":
                            user1 = True
                            pass1 = True
                            statement = ""
                        elif username == "":
                            user1 = True
                            statement = ""
                        elif password == "":
                            pass1 = True
                            statement = ""
                        else:
                            statement = "May be your username or password is wrong"
                        context = {
                            "statement" : statement,
                            "username" : username,
                            "password" : password,
                            "user1" : user1,
                            "pass1" : pass1,
                        }
                        return render(request,"login/login.html",context)

                elif page=="984421":
                    return render(request, "login/forget.html", {"success" : False, "msg" : True})

                elif page=="377666":
                    email=request.POST["email"]
                    if email=="":
                        return render(request, "login/forget.html", {"success" : False, "msg" : True})
                    else:
                        if User.objects.filter(email = email).exists():
                            query = User.objects.get(email = email)
                            username = query.username
                            print username
                            query1 = personmodels.objects.get(email = email)
                            user_id = query1.id
                            print user_id
                            user_id = str(user_id)
                            subject = "Password change for Shatveena.com"
                            message="your username is %s. \n click on http://127.0.0.1:8000/forget_password/%s/id-%s/ link in order to reset your password" %(username, username, user_id)
                            print message
                            # send_mail(subject, message,settings.EMAIL_HOST_USER,[email],fail_silently = False)
                            context={
                                "message" : "open your email to reset your password",
                                "email" : email,
                                "success" : True,
                                "msg" : False,
                            }
                            return render(request, "login/forget.html", context)
                        else:
                            context={
                                "message" : "Your entered email is wrong, try again",
                                "email" : email,
                                "success" : False,
                                "msg" : True
                            }
                            return render(request, "login/forget.html", context)
        else:
            form = login_form()
            return render(request, "login/login.html", {'form' : form,"user" : False, "pass" : False})

# login page view ends here

# logout view starts here

def logout_page(request):
    if request.user.is_authenticated():
        logout(request)
        return HttpResponseRedirect("/")

# logout view ends here

# forget password view starts from here

def forget_password(request,username,id):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/")
    else:
        user = get_object_or_404(User, username=username)
        user_id = get_object_or_404(personmodels, id = id)
        if user and user_id:
            if request.method=="POST":
                password = request.POST["password"]
                confirm_password = request.POST["confirm_password"]
                if password=="":
                    context={
                        "username" : username,
                        "id" : id,
                        "message1" : "Please enter your new password",
                        "confirm_password" : confirm_password,
                    }
                    return render(request, "login/forget_password.html",context)
                else:
                    if len(password)<7:
                        context={
                            "username" : username,
                            "id" : id,
                            "message1" : "Password must have atleast 7 characters",
                            "confirm_password" : confirm_password,
                            "password" : password,
                        }
                        return render(request, "login/forget_password.html",context)
                    else:
                        if password==confirm_password:
                            user = User.objects.get(username = username)
                            user.set_password(password)
                            user.save()
                            print user.password
                            return HttpResponseRedirect("/login/")
                        else:
                            context={
                                "username" : username,
                                "id" : id,
                                "message1" : "Your entered password doesn't match",
                                "confirm_password" : confirm_password,
                                "password" : password,
                            }
                            return render(request, "login/forget_password.html",context)
            else:
                context={
                    "username" : username,
                    "id" : id,
                    "message1" : "Please enter your new password"
                }
                return render(request, "login/forget_password.html",context)

# forget password view ends here
