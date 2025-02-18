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
    