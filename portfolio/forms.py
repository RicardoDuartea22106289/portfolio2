from django import forms
from django.forms import ModelForm
from .models import Post, Disciplina


class TarefaForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
    # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'título post'}),
            'prioridade': forms.NumberInput(attrs={'class': 'form-control', 'max': 3, 'min': 1}),
        }


    # texto a exibir junto à janela de inserção
        labels = {
            'titulo': 'Título',
            'concluido': 'Concluída',
        }


    # texto auxiliar a um determinado campo do formulário
        help_texts = {
            'prioridade': 'prioridade: baixa=1, media=2, alta=3',
        }

class DisciplinaForm(ModelForm):
    class Meta:
        model = Disciplina
        fields = '__all__'
    # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'título post'}),
            'prioridade': forms.NumberInput(attrs={'class': 'form-control', 'max': 3, 'min': 1}),
        }


    # texto a exibir junto à janela de inserção
        labels = {
            'nome': 'Nome',
            'concluido': 'Concluída',
        }


    # texto auxiliar a um determinado campo do formulário
        help_texts = {
            'prioridade': 'prioridade: baixa=1, media=2, alta=3',
        }