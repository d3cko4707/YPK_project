from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from .forms import *

from .models import *
# Create your views here.

def Homepage(request):
    carousel = Pictures.objects.all()
    return render(request, 'home.html', {'carousel':carousel})

def About(request):
    return render(request, 'about.html')

def Event(request):
    return render(request, 'Events.html')

def NewsRoom(request):
    return render(request, 'News_Center.html')

def Membership(request):
    return render(request, 'Member.html')

def Sign_in(request):
    " handling user login and registering "

    form = SignUpForm()

    if request.method == 'POST':
        if 'register' in request.POST:
            form = SignUpForm(request.POST)
            if form.is_valid():
                # We create the user and the customer
                user = User(username=form.cleaned_data['username'], email=form.cleaned_data['email'],
                            first_name=form.cleaned_data['first_name'], last_name=form.cleaned_data['last_name'],
                            )
                user.set_password(form.cleaned_data['password'])
                user.save()
                client = Member(user_id=user.id)
                client.save()

                # We connect the client
                user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
                login(request, user)

                if request.GET.get('next', False):
                    return redirect(request.GET['next'])
                else:
                    return redirect(reverse('commerce:root'))
        else:
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                if user.is_active:
                    client = Member.objects.filter(user_id=user.id).first()
                    login(request, user)
                    if request.GET.get('next', False):
                        return redirect(request.GET['next'])
                    else:
                        return redirect(reverse('web_app:home_page'))
                else:
                    messages.add_message(request, messages.ERROR,
                                         'Your account has been disabled, please contact customer service.')
            else:
                messages.add_message(request, messages.ERROR,
                                     'The identifiers you entered are incorrect !')

    return render(request, 'sing_in.html', {
        'get': request.GET,
        'form': form
    })


def Sign_out(request):
    return HttpResponse('sing_ou')

def Join(request):
    if request.method == 'GET':
       return redirect(reverse('web_app:register_page'))
    else:
        return redirect(reverse('web_app:home_page'))

def Donate(request):
    return HttpResponse('donate_page')

def Register(request):
    "holding the registration of members "
    form = MembershipForm()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    else:
        return render(request, 'register.html', {'form':form})

