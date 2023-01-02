from django.db import models
from django_resized import ResizedImageField


# Create your models here.


class AboutMe(models.Model):
    about = models.TextField()
    resume = models.FileField(upload_to="pdf/")
    image = ResizedImageField(size=[1000, 1000], upload_to="images/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "About Me"
        verbose_name_plural = 'Abouts'


class Greetings(models.Model):
    greet = models.CharField(max_length=120)
    resignation = models.CharField(max_length=120)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Greeting"
        verbose_name_plural = 'Greetings'
