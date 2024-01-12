from rest_framework import serializers
from .models import ImageModel

class ImageUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = ('image','address', )
