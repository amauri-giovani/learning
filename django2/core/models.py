from django.db import models
from stdimage.models import StdImageField
from django.db.models import signals
from django.template.defaultfilters import slugify

# Create your models here.


class Base(models.Model):
    criado = models.DateTimeField('Data De Criação', auto_now_add=True)
    modificado = models.DateTimeField('Data de Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo', default=True)

    class Meta:
        abstract = True


class Curso(Base):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    vagas = models.IntegerField('Vagas')
    imagem = StdImageField('Imagem', upload_to='cursos', variations={'thumb': (124, 124)})
    doc = models.FileField('Documentação', upload_to='cursospdf', default="")
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.nome


def vagas_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)


signals.pre_save.connect(vagas_pre_save, sender=Curso)


