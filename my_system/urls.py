from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('suggest', views.suggest, name='suggest'),
    path('complaints', views.complaints, name='complaints'),
    path('foreignHolidays', views.foreignHoliday, name='holiday_foreign'),
    path('indianHolidays', views.indiaHoliday, name='holiday_india'),
    path('book-tickets', views.bookTickets, name='book_tickets'),
    path('cancel-tickets', views.cancelTickets, name='cancel_tickets'),
    path('search-trains', views.searchTrains, name='search_trains'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('signup2', views.UserFormView.as_view(), name='signup2'),

]
