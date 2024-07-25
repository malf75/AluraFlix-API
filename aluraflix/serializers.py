from aluraflix.validators import *
from rest_framework import serializers
from aluraflix.models import Video, Categoria

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
    def validate(self, data):
        if not cor_valida(data['cor']):
            raise serializers.ValidationError({'cor':'Hexadecimal de cor não válido'})
        return data

class ListaVideosCategorizadosSerializer(serializers.ModelSerializer):
    video_titulo = serializers.ReadOnlyField(source='titulo')
    video_url = serializers.ReadOnlyField(source='url')
    class Meta:
        model = Categoria
        fields = ['video_titulo', 'video_url']