from django.db import models
import datetime
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.


@python_2_unicode_compatible
class Image(models.Model):

    album = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='uploads/')
    posted_date = models.DateTimeField('date posted')

    def __str__(self):
        if self.description is not '':
            return self.description
        else:
            return self.album
