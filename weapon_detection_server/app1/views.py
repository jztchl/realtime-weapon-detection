# In your Django app views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ImageUploadSerializer
from .models import ImageModel
from django.shortcuts import render
from django.http import JsonResponse

@api_view(['POST'])
def upload_image(request):
    if request.method == 'POST':
        image_serializer = ImageUploadSerializer(data=request.data, context={'request': request})
        if image_serializer.is_valid():
            # Save the uploaded image
            image_serializer.save()

            # Get the address data
            address = request.data.get('address', 'No address provided')
            # You can now process or store the address as needed
            print("new upload" + address)
            return Response({'message': 'Image and address uploaded successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def image_list(request):
    last_id = request.GET.get('last_id')

    if last_id:
        try:
            last_id = int(last_id)
        except ValueError:
            return JsonResponse({'error': 'Invalid ID format'}, status=400)

        images = ImageModel.objects.filter(id__gt=last_id)
    else:
        images = ImageModel.objects.all()

    data = [{'image': image.image.url, 'address': image.address,'id': image.id} for image in images]
    return JsonResponse({'images': data})

def index(request):
    return render(request, 'image_list.html')
