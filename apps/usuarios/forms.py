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
    
    def clean_signup_name(self): # o self puxa as informações da classe
        nome = self.cleaned_data.get("signup_name")

        if nome:
            nome = nome.strip()
            if " " in nome:
                raise forms.ValidationError("Espaços não permitidos no campo 'Nome de cadastro'")
            else:
                return nome
            
    def clean_password_2(self):
        senha_1 = self.cleaned_data.get("password_1")
        senha_2 = self.cleaned_data.get("password_2")

        if senha_1 and senha_2:
            if senha_1 != senha_2:
                raise forms.ValidationError("Senhas não coincidem!")
            else:
                return senha_2
