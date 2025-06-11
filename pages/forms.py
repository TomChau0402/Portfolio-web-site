from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length= 250, widget = forms.TextInput(attrs={"placeholder":"Name"}))
    email = forms.CharField(widget=forms.TextInput())
    message = forms.CharField()