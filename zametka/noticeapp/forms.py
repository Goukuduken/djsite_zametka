from django import forms
from .models import *

class AddNotice(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ['title', 'text']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-label',
                                            'id': 'exampleFormControlInput1',
                                            'placeholder': 'Input your title here', }),
            'text': forms.Textarea(attrs={'class': 'form-label',
                                          'id': 'exampleFormControlTextarea1',
                                          'rows': '3',
                                          'placeholder': 'Input your title here', }),
        }