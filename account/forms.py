
"""
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label= '登录')
    password = forms.CharField(widget=forms.PasswordInput,label= '密码')

"""