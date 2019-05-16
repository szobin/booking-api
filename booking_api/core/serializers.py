from django.contrib.auth.models import User, Group
from django.urls import reverse
from .models import Property, Booking
from rest_framework import serializers


'''
class UserSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:user-detail", source='username',
                                               lookup_url_kwarg='username', lookup_field='username')
    email = serializers.EmailField()
    username = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    first_name = serializers.CharField(max_length=100)
'''


class OwnerSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:owner-detail", lookup_field='username')

    email = serializers.EmailField()
    username = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    first_name = serializers.CharField(max_length=100)

    def create(self, validated_data):
        created_user = User.objects.create_user(**validated_data, password="12345")
        created_user.groups.set([1, ])
        created_user.save()
        return created_user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.save()
        return instance


class GuestSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:guest-detail", lookup_field='username')

    email = serializers.EmailField()
    username = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    first_name = serializers.CharField(max_length=100)

    def create(self, validated_data):
        created_user = User.objects.create_user(**validated_data, password="12345")
        created_user.groups.set([2, ])
        created_user.save()
        return created_user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.save()
        return instance


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name',)


class PropertySerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:property-detail", lookup_field='id')
    owner = OwnerSerializer()

    image = serializers.ImageField()
    image_url = serializers.SerializerMethodField()

    def get_image_url(self, prop):
        # returning image url if there is an image else blank string
        if not prop.image:
            return ""
        request = self.context.get('request')
        uri = reverse("property-image", kwargs={"id": prop.pk})
        return request.build_absolute_uri(uri)

    class Meta:
        model = Property
        fields = '__all__'  # ('updated', 'url', 'owner')  #

    def update(self, instance, validated_data):
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance


class BookingSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:booking-detail", lookup_field='id')
    property = PropertySerializer()
    guest = GuestSerializer()

    class Meta:
        model = Booking
        fields = '__all__'
