from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from . import models

from django.contrib.auth.admin import UserAdmin as UserBaseAdmin

@admin.register(models.Node)
class NodeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.UserPosition)
class UserPositionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.User)
class UserAdmin(UserBaseAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": (
            "first_name",
            "last_name",
            "sex",
            "is_teacher",
            "email",
            "phone",
        )}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
