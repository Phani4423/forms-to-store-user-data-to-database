from django.contrib import admin

# Register your models here.
from app.models import *
admin.site.register(game)
admin.site.register(player_info)

