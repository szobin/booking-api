from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.http import HttpResponse
from wsgiref.util import FileWrapper
from rest_framework import viewsets, permissions, status
from .serializers import OwnerSerializer, GuestSerializer, PropertySerializer, BookingSerializer

from rest_framework.response import Response

from .models import Property, Booking


'''
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAdminUser,)

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # lookup_field = 'username'
    # lookup_url_kwarg = 'username'
'''


class OwnerViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAdminUser,)

    queryset = User.objects.filter(is_active=True, groups=1).order_by('-date_joined')  # all()
    serializer_class = OwnerSerializer
    lookup_field = 'username'


class GuestViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAdminUser,)

    queryset = User.objects.filter(is_active=True, groups=2).order_by('-date_joined')  # all()
    serializer_class = GuestSerializer
    lookup_field = 'username'


class PropertyViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAdminUser,)

    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    lookup_field = 'id'


class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAdminUser,)

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class PropertyView(APIView):
    def get(self, request, id):
        try:
            p = Property.objects.get(pk=id)
        except Property.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PropertySerializer(p, context={'request': request})
        return Response(serializer.data)


class PropertyImage(APIView):
    def get(self, request, id):
        try:
            p = Property.objects.get(pk=id)
        except Property.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        image = p.image
        fp = open(image.path, 'rb')
        response = HttpResponse(FileWrapper(fp), content_type='image/png')
        return response


class BookingsView(APIView):
    def get(self, request, format=None):
        bookings = [
            {"name": "Name 1", "item": {"name": "item 1"}, "startTime": "2019-10-02"},
        ]
        return Response(bookings)
