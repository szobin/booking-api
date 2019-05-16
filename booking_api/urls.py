from django.urls import include, path
from django.contrib.auth.views import LoginView
from django.contrib import admin

from rest_framework.authtoken import views as auth_views
from .router import router
from .core import views

# Wire up our API using automatic URL routing.

urlpatterns = [
    path('', include((router.urls, 'api'), 'api')),
    path('api/property/<int:id>/', views.PropertyView.as_view(), name='property-view'),
    path('api/property/<int:id>/img/', views.PropertyImage.as_view(), name='property-image'),
    # path('booking/rest/bookings', views.BookingsView.as_view()),
    path('api-token-auth/', auth_views.obtain_auth_token, name='api_token_auth'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    # path('login/', LoginView.as_view(), name='login')
]
