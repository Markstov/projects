from django import forms
from .models import Buy, Author

class RequestForm(forms.ModelForm):
    class Meta:
        model = Buy
        fields = ['title', 'content','timestamp', 'status', 'status1', 'status2', 'post_author']

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'second_name', 'email']