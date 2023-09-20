from django.contrib import admin
from .models import Venue
from .models import MyClubUser
from .models import Event

admin.site.register(Venue)
admin.site.register(MyClubUser)
admin.site.register(Event)

#To push these databases, we use two-step processes:
#1. make migrations
#2.Push a migration