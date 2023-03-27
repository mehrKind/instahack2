from django import forms

class Getpass(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'id' : 'username',
        'type' : 'name',
        'placeholder' : 'Phone number, username, or email'
    }))

    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={
        'id' : 'username',
        'type' : 'password',
        'placeholder' : 'password'
    }))