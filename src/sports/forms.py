from django import forms
from django.db.models import fields
from .models import Team 

class SearchTeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['teamId', 'city' 'fullName', 'nickname', 'shortName']
        