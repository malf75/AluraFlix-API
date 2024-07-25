from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, permissions
from aluraflix.views import VideosViewSet, CategoriasViewSet, ListaVideosCategorizados, ListaVideosFree, SecureView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

schema_view = get_schema_view(
   openapi.Info(
      title="Aluraflix API",
      default_version='v1',
      description="API de vídeos educacionais desenvolvida para o Alura Challenge de Backend",
      terms_of_service="",
      contact=openapi.Contact(email="malfbf6@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register('videos', VideosViewSet, basename='videos')
router.register('categorias', CategoriasViewSet, basename='categorias')

urlpatterns = [
    path('controle-geral/', admin.site.urls),
    path('', include(router.urls)),
    path('categorias/<int:pk>/videos/', ListaVideosCategorizados.as_view()),
    path('free/', ListaVideosFree.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('secure/', SecureView.as_view(), name='secure_view'),
]