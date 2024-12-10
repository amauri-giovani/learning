from django import forms
from django.core.mail.message import EmailMessage
from .models import Curso


class ContatoForm(forms.Form):
    assunto = forms.CharField(label='Assunto', max_length=100, required=True)
    nome = forms.CharField(label='Usuário', max_length=100, required=True)
    email = forms.EmailField(label='E-mail', max_length=100, required=True)
    senha = forms.CharField(label='Cadastre sua senha', widget=forms.PasswordInput, required=True)

    def send_mail(self):
        assunto = self.cleaned_data['assunto']
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        senha = self.cleaned_data['senha']

        conteudo = f'Assunto:{assunto}\nNome: {nome}\nE-mail:{email}\nSenha:{senha}\nSenha2:{senha2}'
        mail = EmailMessage(
            subject=assunto,
            body=conteudo,
            from_email='contato@fusion.com.br',
            to=['contato@fusion.com.br'],
            headers={'Reply-To': email},
        )
        mail.send()


class CursoModelForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nome', 'preco', 'vagas', 'doc', 'imagem']
