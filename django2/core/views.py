from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import ContatoForm, CursoModelForm
from .models import Curso
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

# Create your views here.


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['curso'] = Curso.objects.all()
        return context


class Login(TemplateView):
    template_name = 'login.html'


class DocView(TemplateView):
    template_name = 'doc.html'

    def get_context_data(self, **kwargs):
        context = super(DocView, self).get_context_data(**kwargs)
        context['curso'] = Curso.objects.all()
        return context


class CursoView(FormView):
    template_name = 'curso.html'
    form_class = CursoModelForm
    success_url = reverse_lazy('index')

    def form_valid(self, form, *args, **kwargs):
        form.save()
        messages.success(self.request, 'Curso cadastrado com sucesso')
        return super(CursoView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao cadastrar curso')
        return super(CursoView, self).form_invalid(form, *args, **kwargs)


class ContatoView(FormView):
    template_name = 'contato.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso, verifique sua caixa de entrada.')
        return super(ContatoView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar e-mail, verifique as informações')
        return super(ContatoView, self).form_invalid(form, *args, **kwargs)
