from django import forms
from .models import ContactusMessage

class MessageForm(forms.ModelForm):
    class Meta:
        model = ContactusMessage
        fields = '__all__'