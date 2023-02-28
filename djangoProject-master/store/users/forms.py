from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms

from .models import User
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите имя пользователя'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class' : 'form-control py-4',
        'placeholder' : 'Введите пароль'
    }))
    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control py-4',
        'placeholder' : 'Введите имя'
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control py-4',
        'placeholder' : 'Введите Фамилию'
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control py-4',
        'placeholder' : 'Введите имя пользователя'
    }))

    # email = forms.EmailField(widget=forms.EmailField(attrs={
    #     'class' : 'form-control py-4',
    #     'placeholder' : 'Введите почту'
    # }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class' : 'form-control py-4',
        'placeholder' : 'Введите пароль'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class' : 'form-control py-4',
        'placeholder' : 'Подтвердите почту'
    }))
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control py-4'
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control py-4',
    }))

    image = forms.ImageField(widget=forms.FileInput (attrs={
        'class' : 'custom-file-input'
    }), required=False)

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control py-4', 'readonly': True
    }))

    # email = forms.CharField(widget=forms.TextInput(attrs={
    #     'class' : 'form-control py-4', 'readonly': True
    # }))
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'image', 'username', 'email')