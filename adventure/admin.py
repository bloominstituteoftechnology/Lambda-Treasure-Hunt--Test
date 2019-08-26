from django.contrib import admin

# Register your models here.


from django.contrib import admin
from .models import Player, Room, Item, Group

admin.site.register((Player, Room, Item, Group))
