from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import UserData


# Define inline admin descriptor for UserData
# (1 to 1 relation with User)
class UserDataInline(admin.StackedInline):
    """
    """

    model = UserData
    can_delete = False
    verbose_name = "Utilisateur"


# Define new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (UserDataInline, )


# un-register default user admin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
