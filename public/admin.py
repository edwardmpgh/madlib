from django.contrib import admin

from .models import MadLibs, WordType, IpAddress, GameParameters

admin.site.register(MadLibs)
admin.site.register(WordType)
admin.site.register(IpAddress)
admin.site.register(GameParameters)