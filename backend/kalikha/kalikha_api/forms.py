from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, ResourceListing, MaterialCategory, ResourceMaterial

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'user_type', 'name', 'description', 'location')

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'user_type', 'name', 'description', 'location', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')

class SignUpForm(forms.ModelForm):
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'password2', 'name', 'description', 'location', 'user_type')
        widgets = {
            'password': forms.PasswordInput(),
            'user_type': forms.RadioSelect(), # Example of a widget
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")
        if password and password2 and password != password2:
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class SignInForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class ResourceListingForm(forms.ModelForm):
    class Meta:
        model = ResourceListing
        exclude = ['provider']

class MaterialCategoryForm(forms.ModelForm):
    class Meta:
        model = MaterialCategory
        fields = '__all__'

class ResourceMaterialForm(forms.ModelForm):
    type = forms.ModelChoiceField(queryset=MaterialCategory.objects.all().order_by('name'))
    resource_listing = forms.ModelChoiceField(queryset=ResourceListing.objects.all().order_by('name'))

    class Meta:
        model = ResourceMaterial
        fields = '__all__'