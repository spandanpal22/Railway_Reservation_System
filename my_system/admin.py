from django.contrib import admin
from .models import Suggestion,UserRegistration

# Register your models here.
admin.site.register(Suggestion)
admin.site.register(UserRegistration)
