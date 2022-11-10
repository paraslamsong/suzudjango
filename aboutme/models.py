from django.db import models

from suzatadjango.utis import image_resize

# Create your models here.


class AboutMe(models.Model):
    about = models.TextField()
    resume = models.FileField(upload_to="pdf/")
    image = models.ImageField(upload_to="images/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, commit=True, *args, **kwargs):
        if commit:
            image_resize(self.image, 1000, 1000)
            super().save(*args, **kwargs)

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
