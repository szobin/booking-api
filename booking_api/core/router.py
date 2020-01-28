from rest_framework import routers
from booking_api.core import views


router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
router.register(r'api/owners', views.OwnerViewSet, basename='owner')
router.register(r'api/guests', views.GuestViewSet, basename='guest')
router.register(r'api/properties', views.PropertyViewSet, basename='property')
router.register(r'api/booking', views.BookingViewSet, basename='booking')
