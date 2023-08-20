from django.contrib import admin
from . import models


@admin.register(models.Node)
class NodeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.UserPosition)
class UserPositionAdmin(admin.ModelAdmin):
    pass
