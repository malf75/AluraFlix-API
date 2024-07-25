from django.test import TestCase
from aluraflix.models import Video, Categoria
from aluraflix.serializers import VideoSerializer, CategoriaSerializer

class VideoSerializerTestCase(TestCase):
    def setUp(self):
        self.video = Video(
            id = 1,
            titulo = 'Video Teste',
            descricao = 'Este é um vídeo de teste',
            url = 'https://www.teste.com/teste',
        )
        self.serializer = VideoSerializer(instance=self.video)

    def test_serialized_fields_check(self):
        """Test to verify serialized fields of video"""
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id','titulo','descricao','url','categoria']))

    def test_content_from_serialized_fields(self):
        """Test to verify content of serialized videos"""
        data = self.serializer.data
        self.assertEqual(data['id'], self.video.id)
        self.assertEqual(data['titulo'], self.video.titulo)
        self.assertEqual(data['descricao'], self.video.descricao)
        self.assertEqual(data['url'], self.video.url)
        self.assertEqual(data['categoria'], [])

class CategoriaSerializerTestCase(TestCase):
    def setUp(self):
        self.categoria = Categoria(
            titulo = 'Categoria Teste',
            cor = '#444440'
        )
        self.serializer = CategoriaSerializer(instance=self.categoria)

    def test_serialized_fields_check(self):
        """Test to verify serialized fields of categoria"""
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id','titulo','cor']))

    def test_content_from_serialized_fields(self):
        """Test to verify content of serialized categorias"""
        data = self.serializer.data
        self.assertEqual(data['id'], self.categoria.id)
        self.assertEqual(data['titulo'], self.categoria.titulo)
        self.assertEqual(data['cor'], self.categoria.cor)