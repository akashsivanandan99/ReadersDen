from allauth.account.forms import SignupForm, LoginForm
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from phonenumber_field.formfields import PhoneNumberField

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email', 'name', 'phone')


class CustomSignupForm(SignupForm):

    def __init__(self, *args, **kwargs):
        # Call the init of the parent class
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['name'] = forms.CharField(required=True)
        self.fields['phone'] = PhoneNumberField(required=True)
        self.fields['email'] = forms.CharField(required=True)

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['phone'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

    # # Put in custom signup logic

    def save(self, request):
        # Ensure you call the parent class's save.
        # .save() returns a User object.

        user = super(CustomSignupForm, self).save(request)
        phone = self.cleaned_data['phone']
        name = self.cleaned_data['name']
        user.phone = phone
        user.name = name
        user.save()
        # Add your own processing here.

        # You must return the original result.
        return user


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    message = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))


class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['remember'].widget.attrs['class'] = 'form-check-input'

    def login(self, *args, **kwargs):
        return super(CustomLoginForm, self).login(*args, **kwargs)


class AddBookForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    summary = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    isbn = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    author = forms.CharField(widget=forms.TextInput(attrs={"class": "form-select"}))
    genre = forms.CharField(widget=forms.TextInput(attrs={"class": "form-select"}))
