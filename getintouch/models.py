from django.db import models

# Create your models here.


class Messages(models.Model):
    full_name = models.CharField(max_length=120)
    email_address = models.CharField(max_length=120)
    subject = models.CharField(max_length=120)
    message = models.TextField()
    is_visited = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = 'Messages'
