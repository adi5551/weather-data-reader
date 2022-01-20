from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase


class TestWeatherReaderAPI(APITestCase):
    '''
    Testcase to test get_weather_data API
    '''

    User = get_user_model()

    def setUp(self):
        self.client = APIClient()
        self.user = self.User.objects.create_superuser('admin', 'admin@admin.com', 'admin123')
        self.token, created = Token.objects.get_or_create(user=self.user)

    def tearDown(self):
        self.User.objects.all().delete()
        Token.objects.all().delete()

    def test_weather_reader_get(self):
        self.client.login(username=self.user.username, password=self.user.password)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + str(self.token))
        response = self.client.get(
            reverse('get_weather_data'),
            data={'parameter': 'Tmin', 'region': 'England_SE_and_Central_S'},
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get(
            reverse('get_weather_data'),
            data={'parameter': 'Tmin'},
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
