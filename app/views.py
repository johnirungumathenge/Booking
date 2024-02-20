from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.hashers import make_password, check_password
from .models import User
from .forms import LoginForm, RegistrationForm
from django.contrib.auth import logout
from django.contrib import messages
from django.core.exceptions import ValidationError

from hearse.models import Hearse, Request

# Create your views here.
def home(request):
    user_id = request.session.get('user_id', None)
    if user_id:
        return render(request, 'index.html', {'user_id': user_id})
    else:
        return redirect('login')

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            try:
                user = User.objects.get(email=email)

                if check_password(password, user.password):
                    request.session['user_id'] = user.id
                    return redirect('home')
                else:
                    messages.error(request, 'Incorrect password.')

            except User.DoesNotExist:
                messages.error(request, 'User with this email does not exist.')

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def register(request):
    # user_id = request.session.get('user_id', None)
    if request.method == 'POST':
       
        form = RegistrationForm(request.POST)
        if form.is_valid():
            fullname = form.cleaned_data['fullname']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            profile_image = form.cleaned_data['profile_image']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']

            if password == confirm_password:
                hashed_password = make_password(password)
                user = User(fullname=fullname,email=email,phone=phone,profile_image=profile_image, password=hashed_password)
                user.save()
                
                return redirect('login')
            else:
                messages.error(request, 'passwords do not match.')
    else:
        form = RegistrationForm()

    return render(request, 'signup.html', {'form': form })


def show(request, user_id):
    person = get_object_or_404(User, id=user_id)
    user_id = person.id
    return render(request, 'show.html', {'person':person, 'user_id':user_id})


# requests
def show_request(request, user_id):
    # req = Request.objects.all()
    req = get_object_or_404(Request, id=user_id)
    user_id = request.session.get('user_id', None)
    context ={
        "requests": req,
        "user_id":user_id
    }
    return render(request, 'request.html',context)

# Hearses
def hearses(request, user_id):
    hearses = Hearse.objects.all()
    user_id = request.session.get('user_id', None)
    context ={
        "hearses":hearses,
        'user_id': user_id,        
    }
    return render(request, 'hearse.html', context)

def user_logout(request):
    # Use Django's logout function to log the user out
    logout(request)
    return redirect('login')
