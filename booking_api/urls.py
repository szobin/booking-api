from django.urls import include, path
from django.contrib import admin

from rest_framework.authtoken import views as auth_views


urlpatterns = [
    path('', include('booking_api.core.urls')),
    path('api-token-auth/', auth_views.obtain_auth_token, name='api_token_auth'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
