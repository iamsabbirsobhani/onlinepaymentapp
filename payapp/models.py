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


class Transaction(models.Model):
    sender = models.ForeignKey("User", on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey("User", on_delete=models.CASCADE, related_name='receiver')
    amount = models.FloatField(default=0.0)
    currency_type = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sender.username + " " + self.receiver.username + " " + str(self.amount) + " " + self.currency_type + " " + str(self.date)


class PaymentRequest(models.Model):
    sender = models.ForeignKey("User", on_delete=models.CASCADE, related_name='sender_payment')
    receiver = models.ForeignKey("User", on_delete=models.CASCADE, related_name='receiver_payment')
    amount = models.FloatField(default=0.0)
    currency_type = models.CharField(max_length=50)
    message = models.CharField(max_length=1000, default="")
    date = models.DateTimeField(auto_now_add=True)
    isAccepted = models.BooleanField(default=False)

    def __str__(self):
        return self.sender.username + " " + self.receiver.username + " " + str(self.amount) + " " + self.currency_type + " " + str(self.date)