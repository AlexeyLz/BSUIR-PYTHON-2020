from django import forms
from django.contrib.auth.models import User
from django.forms import Textarea

from .models import Car, Comments
from django.contrib.auth.forms import AuthenticationForm


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class AuthUserForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def save(self, commit = True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('text',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

