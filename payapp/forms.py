from django import forms


class SignupForm(forms.Form):
    username = forms.CharField(label='username', max_length=50)
    first_name = forms.CharField(label='firstname', max_length=50)
    last_name = forms.CharField(label='lastname', max_length=50, required=False)
    email = forms.CharField(label='email', max_length=50)
    password = forms.CharField(label='password', max_length=50)
    # currency_type = forms.CharField(max_length=50, required=False)