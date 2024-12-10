from django.test import TestCase

from celery_basic.models import Arquivo


class ArquivoTest(TestCase):
    def test_cria_arquivo(self):
        with open("controle_estoque.produto.xls", "rb") as file_upload:
            resp = self.client.post("/upload/", {"nome": "controle_estoque.produto.xls", "arquivo_upload": file_upload})
        file = Arquivo.objects.first()
        with self.subTest():
            self.assertTrue(Arquivo.objects.exists())
            self.assertEqual(200, resp.status_code)
            self.assertEqual(1, len(Arquivo.objects.all()))
            self.assertEqual("controle_estoque.produto.xls", file.nome)
