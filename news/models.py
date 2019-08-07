from django.db import models
from django.utils import timezone


class New(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    published_date = models.DateTimeField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    videofile = models.FileField(upload_to='images', blank=True, null=True)


    def __str__(self):
        return self.title

    def publish(self):
        self.published_date = timezone.now()
        self.save()
