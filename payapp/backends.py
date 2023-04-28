from django.contrib.auth.backends import BaseBackend
from .models import User


class MyAuthBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return None
        if user.check_password(password):
            return user
        else:
            return None
