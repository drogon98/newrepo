from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    # def clean_username(self):
    #     u_name = self.cleaned_data.get("username", 'newuser')
    #     name_objs = User.objects.filter("email").all()
    #     if u_name in name_objs:
    #         raise forms.ValidationError("User with this username alraedy exists")
    #     else:
    #         pass
    #     return u_name

    # def clean_password(self):
    #     password = self.cleaned_data.get("password")
    #     if len(password) < 8:
    #         raise forms.ValidationError("password too short")
    #     return password

    # def clean(self):
    #     cleaned_data=super().clean()
    #     username=cleaned_data['username']
    #     email=cleaned_data['email']
    #     email_objs=User.

    # def clean_email(self):
    #     u_email = self.cleaned_data.get("email")
    #     email_objs = User.objects.filter("email").all()
    #     if u_email in email_objs:
    #         raise forms.ValidationError("User with this email alraedy exists")
    #     else:
    #         pass
    #     return u_email
