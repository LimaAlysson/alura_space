from django import forms 

class LoginForms(forms.Form):
    username = forms.CharField(
        label='Usuario', 
        required=True, 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome de usuario'})
        )
    password = forms.CharField(
        label='Senha', 
        required=True, 
        max_length=70, 
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Senha'})
        )
    
class CadastroForms(forms.Form):
    signup_name = forms.CharField(
        label='Nome de cadastro', 
        required=True, 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome de cadastro'})
        )
    email = forms.EmailField(
        label='Email', 
        required=True, 
        max_length=100,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email@email.com'})
        )
    password_1 = forms.CharField(
        label='Senha', 
        required=True, 
        max_length=70, 
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite sua senha'})
        )
    password_2 = forms.CharField(
        label='Senha', 
        required=True, 
        max_length=70, 
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite sua senha novamente'})
        )