from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length = 50)
    last_name = forms.CharField(max_length = 50)
    email = forms.CharField(max_length = 50)
    address = forms.CharField(max_length = 20)   
    city = forms.CharField(max_length = 50)
    phone = forms.CharField(max_length = 50)



