from django.test import TestCase
from aluraflix.models import Categoria, Video

class CategoriaTestCase(TestCase):
    def setUp(self):
        self.categoria = Categoria(
            titulo = 'Categoria Teste',
            cor = '#444440'
        )

    def test_categoria_atributes_check(self):
        """Test to verify if atributes of a categoria are correct"""
        self.assertEqual(self.categoria.titulo, 'Categoria Teste')
        self.assertEqual(self.categoria.cor, '#444440')

class VideoTestCase(TestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(
            id = 1,
            titulo = 'Categoria Teste',
            cor = '#444440'
        )
        self.video = Video.objects.create(
            id = 1,
            titulo = 'Video Teste',
            descricao = 'Este é um vídeo de teste',
            url = 'https://www.teste.com/teste',
        )
        self.video.categoria.set([1])

    def test_video_atributes_check(self):
        """Test to verify if atributes of a video are correct"""
        self.assertEqual(self.video.titulo, 'Video Teste')
        self.assertEqual(self.video.descricao, 'Este é um vídeo de teste')
        self.assertEqual(self.video.url, 'https://www.teste.com/teste')
        self.assertEqual(list(self.video.categoria.all()), [self.categoria])