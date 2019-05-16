from django.contrib import admin
from .models import Booking, Property, UserContact

# Register your models here.
admin.site.register(Booking)
admin.site.register(Property)
admin.site.register(UserContact)
