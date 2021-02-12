from django import forms

from .models import Contact

class ContactForm(forms.ModelForm):
    """
    Contact Us Submission Form
    """
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'your_message':forms.Textarea(attrs={'rows':7,'cols':40})
        }