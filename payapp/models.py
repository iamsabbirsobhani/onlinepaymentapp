from django.db import models


class User(models.Model):
    currency_type = models.ForeignKey("CurrencyType", on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    balance = models.FloatField(default=0.0)
    role = models.CharField(max_length=50, default="user")

    def __str__(self):
        return self.username


class CurrencyType(models.Model):
    currency_type = models.CharField(max_length=50, default="GBP")

    def __str__(self):
        return self.currency_type