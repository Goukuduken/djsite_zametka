from django import forms
from .models import *

class AddNotice(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ['title', 'text']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'notice-form',
                                            'id': 'notice-form-header',
                                            'placeholder': 'Input your title here', }),
            'text': forms.Textarea(attrs={'class': 'notice-form',
                                          'id': 'exampleFormControlTextarea1',
                                          'rows': '10',
                                          'cols': 30,
                                          'placeholder': 'Input your text here', }),
        }