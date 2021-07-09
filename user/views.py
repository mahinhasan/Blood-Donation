from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .form import*
from django.contrib import messages

from django.contrib.auth import authenticate, login,logout
# Create your views here.



def profile(request):

    if request.method == 'POST':

        user_form = UserUpdate(request.POST or None,instance=request.user)
        profile_form = ProfileUpdate(request.POST or None,request.FILES or None,instance=request.user.userprofile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserUpdate(instance=request.user)
        profile_form = ProfileUpdate(instance=request.user.userprofile)

    context = {
        'user_form':user_form,
        'profile_form':profile_form
    }

    return render(request,'user/profile.html',context)

def signUp(request):
    form = SignUpForm()
    if request.method =='POST':
    
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('b_request')
    else:
        form = SignUpForm()

    context = {
        'form':form,
    }

    return render(request,'user/sign_up.html',context)

def Login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('b_request')
    return render(request,'user/login.html')


def Logout(request):
    logout(request)
    messages.info(request, "You have successfully logged out.") 

    return redirect('/')





