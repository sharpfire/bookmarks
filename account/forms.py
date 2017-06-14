
from django import forms
from django.contrib.auth.models import User
from account.models import Profile


class LoginForm(forms.Form):
    username = forms.CharField(label= '登录')
    password = forms.CharField(widget=forms.PasswordInput,label= '密码')
#丢弃不用的登录表单代码



class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','first_name','email')
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2'] :
            raise forms.ValidationError("Passwords don't match")
        return cd['password']

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email')

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth','photo')
