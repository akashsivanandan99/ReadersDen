from django import forms


class AddBookForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    summary = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    isbn = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    author = forms.CharField(widget=forms.TextInput(attrs={"class": "form-select"}))
