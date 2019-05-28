from django.contrib import admin
from .models import Suggestion,UserRegistration,Train_Data,Ticket

# Register your models here.
admin.site.register(Suggestion)
admin.site.register(UserRegistration)
admin.site.register(Train_Data)
admin.site.register(Ticket)

