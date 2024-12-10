from django.db import models


class Arquivo(models.Model):
    nome = models.CharField(max_length=20)
    arquivo_upload = models.FileField('Upload', upload_to="arquivos_upload", null=True, blank=True)

    class Meta:
        verbose_name = "Arquivo"
        verbose_name_plural = "Arquivos"
        ordering = ["-id"]

    def __str__(self):
        return self.nome
