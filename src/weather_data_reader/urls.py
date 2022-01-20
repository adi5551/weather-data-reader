"""weather_data_reader URL Configuration"""

from django.contrib import admin
from django.urls import path

from users.views import CustomAuthToken
from weather_data_reader.api.views import get_weather_data

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/weather/', get_weather_data, name='get_weather_data'),    # API endpoint
    path('api-token-auth/', CustomAuthToken.as_view(), name='api_auth_token'),
]
