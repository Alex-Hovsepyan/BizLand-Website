from django import forms
from .models import Contact, Subscribe

class ContactModelForm(forms.ModelForm):

    class Meta:

        model = Contact
        fields = ['username', 'email', 'subject', 'message']

class SubscribeModelForm(forms.ModelForm):

    class Meta:

        model = Subscribe
        fields = ['email2']