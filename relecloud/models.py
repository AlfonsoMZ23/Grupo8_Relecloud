from django.db import models
from django.urls import reverse

# Create your models here.
class Destination(models.Model):
    name = models.CharField(
        unique=True,
        null=False,
        blank=False,
        max_length=50
    )
    description = models.TextField(
        max_length=2000,
        null=False,
        blank=False
    )
    slug = models.SlugField()
    image = models.ImageField(
        upload_to='images/',
        default='images/imagenDefault.jpg')

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse('destination_detail', kwargs={"pk": self.pk})

class Cruise(models.Model):
    name = models.CharField(
        unique=True,
        null=False,
        blank=False,
        max_length=50
    )
    description = models.TextField(
        max_length=2000,
        null=False,
        blank=False
    )
    destinations = models.ManyToManyField(
        Destination,
        related_name='cruises',
    )
    def __str__(self) -> str:
        return self.name
    
class InfoRequest(models.Model):
    name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
    )
    email = models.EmailField()
    notes = models.TextField(
        max_length=2000,
        null=False,
        blank=False
    )
    cruise = models.ForeignKey(
        Cruise,
        on_delete=models.PROTECT
    )
    class Meta:
        # Specify the custom table name
        db_table = 'relecloud_inforequest'

class Opinions(models.Model):
    opinion = models.TextField(
        max_length=2000,
        null=False,
        blank=False
    )
    class Meta:
        db_table = 'relecloud_opinions'
