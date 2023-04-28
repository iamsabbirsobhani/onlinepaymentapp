from django.urls import path

from . import views

urlpatterns = [
    path("", views.homePage, name="index"),
    path("login/", views.loginPage, name="login"),
    path("signup/", views.signUp, name="signup"),
    path("signupform/", views.signupForm, name="signupform"),
    path("transferamount/", views.transferMoney, name="transferamount"),
    path("paymentrequest/", views.requestMoney, name="paymentrequest"),
    path("signinform/", views.login_controller, name="signinform"),
    path("logout/", views.logOut, name="logout"),
    path("dashboard/", views.dashboardPage, name="dashboard"),
    path("transfer/", views.transferPage, name="transfer"),
    path("requestpage/", views.requestPage, name="requestpage"),
    path("paymentrequests/", views.paymentRequestPage, name="paymentrequests"),
    path("process_request/", views.process_request, name="process_request"),
]
