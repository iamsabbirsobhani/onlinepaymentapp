from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    balance = models.IntegerField(default=0)
    currency_type = models.CharField(max_length=50, default="GBP")

    def __str__(self):
        return self.username

