from django.shortcuts import render, redirect, HttpResponse

from .models import Suggestion, UserRegistration, Train_Data,Ticket

from django.contrib import messages
from django.http import HttpResponse

from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm

from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import TicketSerializer

import os


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
    if request.method == 'POST':
        from_r = request.POST.get('from')
        to_r = request.POST.get('to')

        req_t = {}
        all_trains = Train_Data.objects.all()

        c = 0
        arr = []
        req_t['trains'] = arr
        req_t['flag'] = 3
        for train in all_trains:
            flag_to = 0
            flag_from = 0
            train_no = train.trainNumber

            filename = '{0}.txt'.format(train_no)

            ts = os.path.join('H:\\Pyharm Projects\\railwayReservationSystem\\uploads\\train_stoppages', filename)

            f = open(ts, "r")
            stops = f.readlines()
            print(stops)
            for stop in stops:
                if to_r + '\n' == stop or to_r == stop:
                    flag_to = 1
                if from_r + '\n' == stop or from_r == stop:
                    flag_from = 1
                if flag_to == 1 and flag_from == 1:
                    req_t['trains'].append(
                        str(train.trainNumber) + "  /  " + str(train.trainName) + "  /  " + str(train.runningDays))
                    req_t['flag'] = 2
                    break

            f.close()
        return render(request, 'my_system/search_trains.html', req_t)

    return render(request, 'my_system/search_trains.html')


def signin(request):
    return render(request, 'my_system/signin.html')


def signup(request):
    return render(request, 'my_system/signup.html')


def suggest(request):
    flag = 0
    if request.method == 'POST':
        name_r = request.POST.get('Name')
        email_r = request.POST.get('Email')
        suggestion_r = request.POST.get('Suggestion')

        s = Suggestion(name=name_r, email=email_r, suggestion=suggestion_r)
        s.save()

        flag = 1

        return render(request, 'my_system/index.html', {'flag': flag})
    else:
        return render(request, 'my_system/index.html', {'flag': flag})


class UserFormView(View):
    form_class = UserForm
    template_name = 'my_system/signup.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(
                commit=False)  # this will save the entered data in user object but won't save in database

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


"""
API Part below
"""


class TicketView(APIView):
    def get(self, request):
        tickets = Ticket.objects.all()
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = TicketSerializer(tickets, many=True)
        return Response({"tickets": serializer.data})

    def post(self, request):
        ticket = request.data.get('ticket')

        """
        # Create an article from the above data
        serializer = ArticleSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
            return Response({"success": "Article '{}' created successfully".format(article_saved.title)})

            """

        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):

        saved_ticket = get_object_or_404(Ticket.objects.all(), pk=pk)
        serializer = TicketSerializer(saved_ticket, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # Get object with this pk
        ticket = get_object_or_404(Ticket.objects.all(), pk=pk)
        ticket.delete()
        return Response({"message": "Ticket with id `{}` has been deleted.".format(pk)}, status=204)

