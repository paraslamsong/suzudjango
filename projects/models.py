from django.db import models
from django_resized import ResizedImageField

# Create your models here.


class Projects(models.Model):
    name = models.CharField(max_length=120)
    info = models.CharField(max_length=120, default="")
    image = ResizedImageField(size=[1000, 1000], upload_to="images/")
    link = models.CharField(max_length=120, null=True)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = 'Projects'
