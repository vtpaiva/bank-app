from .models import User
from django.forms import ModelForm, PasswordInput

class SignUpForm(ModelForm):
    class Meta:
        model = User
        fields = ['CPF', 'first_name', 'last_name', 'email', 'password']
        widgets = {
            'password': PasswordInput(attrs={'placeholder': 'Enter your password'}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password']) 
        if commit:
            user.save()
        return user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['CPF'].widget.attrs.update({'placeholder': 'Enter your CPF'})
        self.fields['first_name'].widget.attrs.update({'placeholder': 'Enter your first name'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Enter your last name'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Enter your e-mail'})