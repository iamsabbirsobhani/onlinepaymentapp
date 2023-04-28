from django.contrib import admin

# Register your models here.

from .models import User, CurrencyType, Transaction, PaymentRequest

admin.site.register(User)
admin.site.register(CurrencyType)
admin.site.register(Transaction)
admin.site.register(PaymentRequest)
