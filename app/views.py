from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from multiprocessing import context
from django.shortcuts import render
from django.views.generic.base import RedirectView
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from app.models import*
from .models import Room ,Topic ,Message
from.forms import RoomForm
from django.contrib.auth.models import User
# for when login some one then shwo tha PAGES
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

def loginPage(request):
    page='login'
    if request.method=='POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)

        except:
            messages.error(request,'enter corrrect user and password')

        user= authenticate(request,username=username,password=password)
       
        if user is not None:
            login(request,user)
            return redirect ('home')
        else:
            messages.error(request,'username or password not exist')
        
    context={'login':login}
    return render(request,'base/login.html',context)


def logoutPage(request):
    logout(request)
    return redirect('home')


'''Sign Up And Redirecting to profile page '''
def registerPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if User.objects.filter(username=username).first():
            messages.warning(request,"Username already exists")
            return redirect("registerPage")
        else:
            a = User.objects.create_user(username,password1,password2)
            a.save()
            if a:
                user = authenticate(username=username,password=password1)
                if user is not None:
                    login(request,user)
                    return redirect('uploadprofile')
    context={}
    return render(request,'base/register.html',context)

def homePage(request):
    rooms= Room.objects.all()
    context={'rooms':rooms}
    return render(request,'base/home.html',context)

def profile_upload(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            name = request.POST['name']
            email = request.POST['email']
            phone_no = request.POST['phoneno']
            location = request.POST['location']
            skill = request.POST['skill']
            bio = request.POST['bio']
            profile_pic = request.FILES['file']
            profile_upload = Profilemodel.objects.create(name=name,email=email,skills=skill,location=location,phone_no=phone_no,image=profile_pic,bio=bio,user=request.user)
            if profile_upload:
                return redirect("profile")
            else:
                return HttpResponse("Error! Please Try Again Later")
        return render(request,"base/profile-upload.html")
    else:
        return redirect("signup")

def profile(request):
    if request.user.is_authenticated:
        profiles = Profilemodel.objects.get(user=request.user)
        posts = Post.objects.all()
        context={'profiles':profiles,'posts':posts}
        return render(request,"base/profile.html",context)
    else:
        return redirect("/registerPage")

def uploadpost(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            profile = Profilemodel.objects.get(user=request.user) 
            postdesc = request.POST['desc']
            file = request.FILES['file']
            posts = Post.objects.create(post=file,profileuser=profile,user=request.user,caption=postdesc)
        return render(request,'base/post.html')
    else:
        return redirect("registerPage")


def roomPage(request,pk):
    room= Room.objects.get(id=pk)
    rmall= Room.objects.all()
    room_messages = room.message_set.all()

    if request.method=='POST':
        message= Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body'))
        return redirect('room',pk=room.id)

    context= {'room':room,'room_messages':room_messages,'rmall':rmall}
    return render(request,'base/chatroom.html',context)


@login_required(login_url ='loginPage')
# jyre bhi koy kam karvanu hoy to login reva j joyye ena mate decoreter vapray  and login ni rey to login url thi login page ma jay rey
def creatRoom(request):
    form = RoomForm

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')


    context= {'form':form}
    return render(request,'base/roomForm.html',context)


@login_required(login_url ='loginPage')
def deleteRoom(request,pk):
    room=Room.objects.get(id=pk)



    if request.method == 'POST':
        room.delete()
        return redirect('home')
    context= {'obj':room}
    return render(request,'base/dalate.html',context)