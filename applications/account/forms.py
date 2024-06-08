# forms.py
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'password1', 'password2')

from django import forms
from .models import CustomUser

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['name', 'surname', 'email', 'phone_number', 'date_of_birth']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and CustomUser.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('Этот адрес электронной почты уже используется.')
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        # Дополнительные проверки для номера телефона, если необходимо
        return phone_number

    from django import forms
    from django.contrib.auth.forms import UserCreationForm
    from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
        email = forms.EmailField(required=True, label="Email")
        name = forms.CharField(required=True, label="Имя")
        surname = forms.CharField(required=True, label="Фамилия")
        phone_number = forms.CharField(required=False, label="Номер телефона")
        date_of_birth = forms.DateField(required=False, label="Дата рождения")

        class Meta:
            model = CustomUser
            fields = ('email', 'name', 'surname', 'phone_number', 'date_of_birth', 'password1', 'password2')

        def save(self, commit=True):
            user = super().save(commit=False)
            user.email = self.cleaned_data['email']
            user.name = self.cleaned_data['name']
            user.surname = self.cleaned_data['surname']
            user.phone_number = self.cleaned_data['phone_number']
            user.date_of_birth = self.cleaned_data['date_of_birth']

            if commit:
                user.save()
            return user
