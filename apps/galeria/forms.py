from django import forms

from apps.galeria.models import Fotografia

#criando form através de um model existente
class FotografiaForms(forms.ModelForm):
    class Meta:
        model = Fotografia
        exclude = ['publicada'] #campos que não são necessarios no form
        labels = {
            'descricao':'Descrição',
            'data_fotografia':'Data de registro',
            'usuario': 'Usuário',
            'foto': 'Arquivo'
        }

        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'legenda': forms.TextInput(attrs={'class':'form-control'}),
            'categoria': forms.Select(attrs={'class':'form-control'}),
            'descricao': forms.Textarea(attrs={'class':'form-control'}),
            'foto': forms.FileInput(attrs={'class':'form-control'}),
            'data_fotografia': forms.DateInput(
                format = '%d/%m/%Y',
                attrs={
                    'type':'date',
                    'class':'form-control'
                    }
            ),
            'usuario': forms.Select(attrs={'class':'form-control'}),
        }