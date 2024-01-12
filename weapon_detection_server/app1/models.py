from django.db import models

class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/')
    address = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Image {self.pk}"