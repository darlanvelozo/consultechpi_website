from django import forms
from .models import Contato, Newsletter, Servico

class ContatoForm(forms.ModelForm):
    """Formulário de contato"""
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'telefone', 'empresa', 'tipo_contato', 'assunto', 'mensagem', 'servico_interesse', 'orcamento_estimado']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Seu nome completo'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'seu@email.com'
            }),
            'telefone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '(11) 99999-9999'
            }),
            'empresa': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome da sua empresa (opcional)'
            }),
            'tipo_contato': forms.Select(attrs={
                'class': 'form-control'
            }),
            'assunto': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Assunto da mensagem'
            }),
            'mensagem': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Descreva sua necessidade ou dúvida...'
            }),
            'servico_interesse': forms.Select(attrs={
                'class': 'form-control'
            }),
            'orcamento_estimado': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Faixa de orçamento (opcional)'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtrar apenas serviços ativos
        self.fields['servico_interesse'].queryset = Servico.objects.filter(ativo=True)
        
        # Tornar alguns campos obrigatórios
        self.fields['nome'].required = True
        self.fields['email'].required = True
        self.fields['assunto'].required = True
        self.fields['mensagem'].required = True

class NewsletterForm(forms.ModelForm):
    """Formulário de inscrição na newsletter"""
    class Meta:
        model = Newsletter
        fields = ['email', 'nome']
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Seu melhor email'
            }),
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Seu nome (opcional)'
            }),
        }
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Newsletter.objects.filter(email=email, ativo=True).exists():
            raise forms.ValidationError('Este email já está inscrito na nossa newsletter.')
        return email

class OrcamentoForm(forms.Form):
    """Formulário específico para orçamentos"""
    nome = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Seu nome completo'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'seu@email.com'
        })
    )
    telefone = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '(11) 99999-9999'
        })
    )
    empresa = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nome da sua empresa'
        })
    )
    servicos_interesse = forms.ModelMultipleChoiceField(
        queryset=Servico.objects.filter(ativo=True),
        widget=forms.CheckboxSelectMultiple(attrs={
            'class': 'form-check-input'
        }),
        required=False
    )
    descricao_projeto = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 5,
            'placeholder': 'Descreva seu projeto, necessidades e objetivos...'
        })
    )
    prazo_desejado = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Prazo desejado para conclusão'
        })
    )
    orcamento_estimado = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Faixa de orçamento disponível'
        })
    )
    urgencia = forms.ChoiceField(
        choices=[
            ('baixa', 'Baixa - Posso esperar'),
            ('media', 'Média - Preciso em algumas semanas'),
            ('alta', 'Alta - Preciso urgentemente'),
        ],
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    ) 