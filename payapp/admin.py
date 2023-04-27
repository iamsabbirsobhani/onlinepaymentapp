from django.contrib import admin

# Register your models here.

from .models import User, CurrencyType

admin.site.register(User)
admin.site.register(CurrencyType)
