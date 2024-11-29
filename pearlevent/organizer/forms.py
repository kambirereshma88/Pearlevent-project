from django import forms
from organizer.models import Organizer

class OrganizerForm(forms.ModelForm):
    class Meta:
        model = Organizer
        fields = ['title', 'description', 'location']
