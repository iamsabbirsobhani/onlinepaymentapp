from django.urls import path

from . import views

urlpatterns = [
    path("", views.homePage, name="index"),
    path("login/", views.loginPage, name="login"),
    path("signup/", views.signUp, name="signup"),
    path("signupform/", views.signupForm, name="signupform"),
    path("transferamount/", views.transferMoney, name="transferamount"),
    path("signinform/", views.login_controller, name="signinform"),
    path("logout/", views.logOut, name="logout"),
    path("dashboard/", views.dashboardPage, name="dashboard"),
    path("transfer/", views.transferPage, name="transfer"),
]
