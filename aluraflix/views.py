from rest_framework import viewsets, generics
from aluraflix.models import Video, Categoria
from aluraflix.serializers import VideoSerializer, CategoriaSerializer, ListaVideosCategorizadosSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

class SecureView(APIView):
    permission_classes=[IsAuthenticated]

    def get(self, request):
        return Response({"message": "You are authenticated!"}, status=status.HTTP_200_OK)

class VideosViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    search_fields = ['titulo']
    ordering_fields = ['titulo']
    permission_classes = [IsAuthenticated]

class CategoriasViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    search_fields = ['titulo']
    ordering_fields = ['titulo']
    permission_classes = [IsAuthenticated]

class ListaVideosCategorizados(generics.ListAPIView):
    def get_queryset(self):
        queryset = Video.objects.filter(categoria=self.kwargs['pk'])
        return queryset
    serializer_class = ListaVideosCategorizadosSerializer
    permission_classes = [IsAuthenticated]

class ListaVideosFree(generics.ListAPIView):
    def get_queryset(self):
        queryset = Video.objects.all()[:10]
        return queryset
    serializer_class = VideoSerializer
    permission_classes = [AllowAny]
    print('test')