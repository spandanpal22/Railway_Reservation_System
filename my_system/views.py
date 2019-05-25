from django.shortcuts import render, redirect
from .models import Suggestion, UserRegistration

from django.contrib import messages
from django.http import HttpResponse

from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm


# Create your views here.

def index(request):
    return render(request, 'my_system/index.html')


def complaints(request):
    return render(request, 'my_system/complaints.html')


def foreignHoliday(request):
    return render(request, 'my_system/holiday_foreign.html')


def indiaHoliday(request):
    return render(request, 'my_system/holiday_india.html')


def bookTickets(request):
    return render(request, 'my_system/book_tickets.html')


def cancelTickets(request):
    return render(request, 'my_system/cancel_tickets.html')


def searchTrains(request):
    return render(request, 'my_system/search_trains.html')


def signin(request):
    return render(request, 'my_system/signin.html')


def signup(request):
    return render(request, 'my_system/signup.html')


def suggest(request):
    flag=0
    if request.method == 'POST':
        name_r = request.POST.get('Name')
        email_r = request.POST.get('Email')
        suggestion_r = request.POST.get('Suggestion')

        s = Suggestion(name=name_r, email=email_r, suggestion=suggestion_r)
        s.save()

        flag=1

        return render(request,'my_system/index.html',{'flag':flag})
    else:
        return render(request, 'my_system/index.html',{'flag':flag})


class UserFormView(View):
    form_class = UserForm
    template_name = 'my_system/signup.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)  # this will save the entered data in user object but won't save in database

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user.set_password(password)

            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')

        return render(request, self.template_name, {'form': form})
