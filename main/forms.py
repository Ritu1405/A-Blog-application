from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    email = forms.EmailField(required = True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

        def save(self, commit = True):
            user = super(UserForm, self).save(commit=False)
            user.email = self.cleaned_data['email']
            if commit:
                user.save()
            return user

class CommentForm(forms.Form):
    author = forms.CharField(max_length = 60,
                            widget = forms.TextInput(attrs = { "class": "form-control", "placeholder" : "Your Name"}))

    body = forms.CharField(widget = forms.Textarea(attrs = {
                                                            "class": "form-control",
                                                            "placeholder": "Leave a comment!"}))