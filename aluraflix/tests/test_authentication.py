from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

class AuthenticationUserVideosTestCase(APITestCase):
    def setUp(self):
        self.list_url_videos = reverse('videos-list')
        self.list_url_categorias = reverse('categorias-list')
        self.user = User.objects.create_user('testuser', password='testuser')

    def test_auth_of_user_with_correct_credentials(self):
        """Test to verify authentication of a user with correct credentials"""
        user = authenticate(username='testuser', password='testuser')
        self.assertTrue((user is not None) and user.is_authenticated)
    
    def test_auth_of_user_with_incorrect_username(self):
        """Test to verify authentication of a user with incorrect credentials"""
        user = authenticate(username='testwrong', password='testuser')
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_auth_of_user_with_incorrect_password(self):
        """Test to verify authentication of a user with incorrect credentials"""
        user = authenticate(username='testuser', password='testwrong')
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_not_authorized_GET(self):
        """Test to verify GET method without authentication"""
        response_videos = self.client.get(self.list_url_videos)
        response_categorias = self.client.get(self.list_url_categorias)
        self.assertEqual(response_videos.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response_categorias.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_authorized_GET(self):
        """Test to verify GET method authenticated"""
        self.client.force_authenticate(self.user)
        response_videos = self.client.get(self.list_url_videos)
        response_categorias = self.client.get(self.list_url_categorias)
        self.assertEqual(response_videos.status_code, status.HTTP_200_OK)
        self.assertEqual(response_categorias.status_code, status.HTTP_200_OK)

class SecureViewTestCase(APITestCase):

    def setUp(self):
        self.list_url_videos = reverse('videos-list')
        self.list_url_categorias = reverse('categorias-list')
        self.url_secure = reverse('secure_view')
        self.user = User.objects.create_user('testuser', password='testuser')
    
    def get_tokens_for_user(self):
        refresh = RefreshToken.for_user(self.user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
    
    def test_secure_view_authenticated(self):
        tokens = self.get_tokens_for_user()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + tokens['access'])
        response = self.client.get(self.url_secure)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_secure_view_unauthenticated(self):
        response = self.client.get(self.url_secure)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)