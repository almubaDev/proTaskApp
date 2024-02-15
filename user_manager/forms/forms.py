from django import forms
from django.contrib.auth.forms import (AuthenticationForm, UserCreationForm,
                                       PasswordChangeForm, PasswordResetForm)
from ..models import CustomUser



class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = "La contraseña no puede parecerse a la anterior, ni ser totalmente numérica, ni tener menos de 8 caracteres."
        
    class Meta:
        model = CustomUser
        fields = ('email', 'full_name', 'country', 'password1', 'password2')


class CustomUserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = forms.EmailInput(attrs={'placeholder': 'Correo electrónico'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'placeholder': 'Contraseña'})    
        
    class Meta:
        model = CustomUser
        fields = ('email', 'password')


class CustomChangePasswordForm(PasswordChangeForm):
    class Meta:
        model: CustomUser
        fields = ('password1', 'password2')
        
        
class CustomResetPasswordForm(PasswordResetForm):
    class Meta:
        model: CustomUser
        fields = ('email')