from django import forms
from django.contrib.auth.forms import (AuthenticationForm, UserCreationForm,
                                       PasswordChangeForm, PasswordResetForm)
from django_countries import countries
from ..models import CustomUser



class CustomUserCreationForm(UserCreationForm):
    countries_list = list(countries)
    countries_list.insert(0, ('', 'Seleccionar país'))
    country = forms.ChoiceField(choices=countries_list)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = "La contraseña no debe tener similitud con otra información del usuario, ni ser totalmente numérica, ni tener menos de 8 caracteres."
        self.fields['email'].widget = forms.EmailInput(attrs={'placeholder': 'Correo electrónico'})
        self.fields['full_name'].widget = forms.TextInput(attrs={'placeholder': 'Nombres Apellidos'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': 'Contraseña'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': 'Repita la contraseña'})
       
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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['new_password1'].help_text = "La contraseña no debe tener similitud con otra información del usuario, ni ser totalmente numérica, ni tener menos de 8 caracteres."
        self.fields['old_password'].widget = forms.PasswordInput(attrs={'placeholder': 'Contraseña actual'})
        self.fields['new_password1'].widget = forms.PasswordInput(attrs={'placeholder': 'Contraseña nueva'})
        self.fields['new_password2'].widget = forms.PasswordInput(attrs={'placeholder': 'Repita la nueva contraseña'})
       
    class Meta:
        model: CustomUser
        fields = ('password1', 'password2')
        
        
class CustomResetPasswordForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget = forms.EmailInput(attrs={'placeholder': 'Correo electrónico vinculado a su cuenta Protask'})
 
    class Meta:
        model = CustomUser
        fields = ('email',)