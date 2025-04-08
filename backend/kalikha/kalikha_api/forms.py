from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class ResourceProviderSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('user_type',)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 'provider'
        if commit:
            user.save()
        return user

class UpcyclerSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('user_type',)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 'upcycler'
        if commit:
            user.save()
        return user