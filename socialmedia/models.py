from django.db import models

# Create your models here.


class SocialMedias(models.Model):
    image = models.ImageField(upload_to="icon/")
    name = models.CharField(max_length=120)
    link = models.CharField(max_length=120)
    description = models.TextField(default=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Social Media"
        verbose_name_plural = 'Social Medias'
