from django.db import models

# Create your models here.


class Services(models.Model):
    icon = models.ImageField(upload_to="icon/")
    title = models.CharField(max_length=120)
    description = models.TextField()

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = 'Services'
