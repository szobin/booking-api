from django.db import models
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User

CONTACT_KINDS = (
    ("TMOB", "Mobile phone"),
    ("EML", "E-mail"),
    ("SKP", "Skype ID"),
)

fs = FileSystemStorage(location='static/files')


class UserContact(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    kind = models.CharField(max_length=4, choices=CONTACT_KINDS)
    value = models.CharField(max_length=120)

    def __str__(self):
        return "{}: {}.{}".format(self.user, self.kind, self.value)


class Property(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    descr = models.TextField()
    image = models.ImageField(storage=fs, upload_to='properties')
    address = models.CharField(max_length=180)
    base_price = models.DecimalField(max_digits=6, decimal_places=2)
    weekend_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    week_discount = models.DecimalField(max_digits=6, decimal_places=3, null=True, blank=True)
    minimal_duration = models.IntegerField(default=1)
    lock_start = models.DateField(null=True, blank=True)
    lock_finish = models.DateField(null=True, blank=True)

    def __str__(self):
        return "{} ({})".format(self.name, self.owner)

    class Meta:
        verbose_name_plural = "properties"
        ordering = ('updated',)


class Booking(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    started = models.DateField()
    finished = models.DateField()
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    guest = models.ForeignKey(User, on_delete=models.CASCADE)
    canceled = models.BooleanField(default=False)
    info2owner = models.TextField()
    amount = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return "{}: {}-{}: ({})".format(self.guest, self.started, self.finished, self.property)

    class Meta:
        ordering = ('created',)
