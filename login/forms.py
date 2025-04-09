from django import forms
from .models import Persona

class login(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre','edad','diagnostico','updrs']
        widgets = {
            'nombre':forms.Textarea(attrs={'rows': 5,
                'cols': 40,
                'style': 'resize: none; width: 500px; height: 15px;'}),
            'diagnostico': forms.Textarea(attrs={
                'rows': 5,
                'cols': 40,
                'style': 'resize: none; width: 700px; height: 100px;'
            })
        }