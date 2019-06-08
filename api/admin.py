from django.contrib import admin

# Register your models here.

from api.models import (
    NavigationMenu, NavigationTab
)

admin.site.register(NavigationMenu)
admin.site.register(NavigationTab)