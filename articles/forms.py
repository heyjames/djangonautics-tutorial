from django import forms
from . import models

class CreateArticle(forms.ModelForm): # This is similar to the "from ... import..." line in accounts/views.py: UserCreationForm, AuthenticationForm
    class Meta:
        model = models.Article
        fields = ['title', 'body', 'slug', 'thumb']
