# from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import force_authenticate
from rest_framework.test import APIRequestFactory
import json
import datetime

from django.contrib.auth.models import User
from .models import Booking, Property
from .views import BookingsView


# Create your tests here.


class TestAPI(APITestCase):

    def setUp(self):
        self.g = User.objects.create(username="guest")
        self.o = User.objects.create(username="owner")
        self.p = Property.objects.create(owner=self.o, name="test house", descr="test house descr",
                                         address="test street", base_price=400.15)
        Booking.objects.create(started=datetime.datetime.now(),
                               finished=datetime.datetime.now()+datetime.timedelta(days=12),
                               property=self.p, guest=self.g, info2owner="info test", amount=10.12)

    def test_categories(self):
        factory = APIRequestFactory()
        view = BookingsView.as_view()

        url = reverse('api:booking-list')
        # resp = self.client.get(url, {})
        request = factory.get(url, {})

        resp = view(request)
        # self.assertEqual(resp.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        request = factory.get(url, {})
        force_authenticate(request, user=self.o)

        resp = view(request)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        # s = resp.data
        # resp_data = json.loads(s)
        self.assertEqual(len(resp.data), 1)

