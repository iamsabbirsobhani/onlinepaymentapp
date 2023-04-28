import json

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User, CurrencyType
import requests
from .backends import MyAuthBackend


def homePage(request):
    user_id = request.session.get('userid')
    if user_id is not None:
        user = User.objects.get(id=user_id)
        return render(request, 'payapp/dashboardPage.html', {'user': user})
    else:
        return render(request, 'payapp/homePage.html')


def loginPage(request):
    return HttpResponse(render(request, 'payapp/loginPage.html'))


def login_controller(request):
    # Handle form submission
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email, password)

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            error_msg = 'User does not exist.'
            request.session.flush()
            return render(request, 'payapp/loginPage.html', {'error_msg': error_msg})

        if user is not None:
            # Log in user
            if user.password == password:
                request.session['userid'] = user.id
                # Redirect to homepage or other view
                return render(request, 'payapp/dashboardPage.html', {'user': user})
            else:
                # Show error message
                request.session.flush()
                error_msg = 'Invalid username or password.'
                return render(request, 'payapp/loginPage.html', {'error_msg': error_msg})

    # Render login form
    return render(request, 'payapp/loginPage.html')


def dashboardPage(request):
    user_id = request.session.get('userid')
    if user_id is not None:
        user = User.objects.get(id=user_id)
        return render(request, 'payapp/dashboardPage.html', {'user': user})
    else:
        return render(request, 'payapp/loginPage.html')


def signupForm(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password1']
        currency_type = request.POST['currency']
        user = User()
        user.username = username
        user.first_name = firstname
        user.last_name = lastname
        user.email = email
        user.password = password
        user.currency_type = CurrencyType.objects.get(pk=currency_type)

        # RESTful Web Service for currency conversion
        if user.currency_type.currency_type == "GBP":
            response = requests.get("http://127.0.0.1:8000/register/gbp_to_usd/1000")
            if response.status_code == 200:
                print(response.content)
                user.balance = response.content
        elif user.currency_type.currency_type == "USD":
            response = requests.get("http://127.0.0.1:8000/register/usd_to_gbp/1000")
            if response.status_code == 200:
                print(response.content)
                user.balance = response.content

        user.save()
        userdata = User.objects.get(id=user.pk)
        request.session['userid'] = userdata.id
        print("User saved")
        return render(request, 'payapp/dashboardPage.html', {'user': userdata})
    else:
        return render(request, 'payapp/signupPage.html')


def signUp(request):
    return HttpResponse(render(request, 'payapp/signupPage.html'))


def transferPage(request):
    user_id = request.session.get('userid')
    if user_id is not None:
        user = User.objects.get(id=user_id)
        return render(request, 'payapp/transferPage.html', {'user': user})
    else:
        return render(request, 'payapp/loginPage.html')


def logOut(request):
    request.session.flush()
    return render(request, 'payapp/homePage.html')


def transferMoney(request):
    user_id = request.session.get('userid')
    if user_id is not None:
        if request.method == 'POST':
            email = request.POST['email']
            amount = request.POST['amount']
            password = request.POST['password']
            user = User.objects.get(id=user_id)
            if user.password == password:
                try:
                    receiver = User.objects.get(email=email)
                except User.DoesNotExist:
                    error_msg = 'User does not exist.'
                    return render(request, 'payapp/transferPage.html', {'user': user, 'error_user': error_msg, 'error_msg': ''})

                if receiver is not None:
                    # Log in user
                    if float(amount) <= user.balance:
                        if receiver.currency_type.currency_type == "GBP" and user.currency_type.currency_type == "GBP":
                            receiver.balance += float(amount)
                            user.balance = user.balance - float(amount)
                        elif receiver.currency_type.currency_type == "USD" and user.currency_type.currency_type == "USD":
                            receiver.balance += float(amount)
                            user.balance = user.balance - float(amount)
                        elif receiver.currency_type.currency_type == "GBP":
                            url = "http://127.0.0.1:8000/register/usd_to_gbp/" + str(amount)
                            response = requests.get(url)
                            if response.status_code == 200:
                                conversion_rate = float(response.content.decode())
                                receiver.balance += conversion_rate
                                user.balance = user.balance - float(amount)
                                print("Receiver balance ", receiver.balance)
                        elif receiver.currency_type.currency_type == "USD":
                            url = "http://127.0.0.1:8000/register/gbp_to_usd/" + str(amount)
                            response = requests.get(url)
                            if response.status_code == 200:
                                conversion_rate = float(response.content.decode())
                                receiver.balance += conversion_rate
                                user.balance = user.balance - float(amount)
                                print('Receiver balance ', receiver.balance)
                        else:
                            error_msg = 'Invalid currency type.'
                            return render(request, 'payapp/transferPage.html', {'user': user, 'error_msg': error_msg})

                        user.save()
                        receiver.save()
                        # Redirect to homepage or other view
                        return render(request, 'payapp/dashboardPage.html', {'user': user})
                    else:
                        # Show error message
                        error_msg = 'Insufficient balance.'
                        return render(request, 'payapp/transferPage.html', {'user': user, 'error_balance': error_msg, 'error_msg': ''})
            else:
                # Show error message
                error_msg = 'Invalid password.'
                return render(request, 'payapp/transferPage.html', {'user': user, 'error_msg': error_msg})
    else:
        return render(request, 'payapp/loginPage.html')