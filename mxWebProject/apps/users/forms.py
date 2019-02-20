from django import forms

class LoginForm(forms.Form):
    #这里的变量名一定要合html的input的name一样
    username=forms.CharField(required=True)
    password=forms.CharField(required=True)