from django.db import models

# Create your models here.


class Service(models.Model):
    name = models.CharField(max_length=200, null=True)
    slug = models.SlugField(max_length=255, null=True, unique=True)
    description = models.CharField(max_length=2000, null=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ""
        return url
