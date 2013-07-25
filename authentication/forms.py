from django import forms as newform

class LoginForm(newform.Form):
    username = newform.CharField()
    password = newform.CharField(widget=newform.PasswordInput)
