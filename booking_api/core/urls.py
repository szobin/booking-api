from django.urls import include, path

from .router import router
from . import views


urlpatterns = [
    path('', include((router.urls, 'api'), 'api')),
    path('api/property/<int:id>/', views.PropertyView.as_view(), name='property-view'),
    path('api/property/<int:id>/img/', views.PropertyImage.as_view(), name='property-image'),
]
