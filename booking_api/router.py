from rest_framework import routers
from booking_api.core import views


router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
router.register(r'api/owners', views.OwnerViewSet, base_name='owner')
router.register(r'api/guests', views.GuestViewSet, base_name='guest')
router.register(r'api/properties', views.PropertyViewSet, base_name='property')
router.register(r'api/booking', views.BookingViewSet, base_name='booking')
