from django.db import models

from suzatadjango.utis import image_resize

# Create your models here.


class Projects(models.Model):
    name = models.CharField(max_length=120)
    info = models.CharField(max_length=120, default="")
    image = models.ImageField(upload_to="images/")
    link = models.CharField(max_length=120, null=True)

    def save(self, commit=True, *args, **kwargs):
        if commit:
            image_resize(self.image, 1000, 1000)
            super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = 'Projects'
