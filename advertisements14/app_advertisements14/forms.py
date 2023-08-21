from django import forms
from .models import Advertisements14
from django.core.exceptions import ValidationError

class Advertisements14Form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['description'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['price'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['auction'].widget.attrs['class'] = 'form-check-input'
        self.fields['connection'].widget.attrs['class'] = 'form-check-input'
        self.fields['image'].widget.attrs['class'] = 'form-control form-control-lg'

    class Meta:
        model = Advertisements14
        fields = ['title', 'description', 'price', 'auction', 'connection', 'image']

    def clean_recipients(self):
        title = self.cleaned_data['title']
        if title.startswith('?'):
            raise ValidationError("Заголовок не может начинаться с вопросительного знака")
        return title

