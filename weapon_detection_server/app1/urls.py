from app1 import views
from django.urls import path

urlpatterns = [
    path("upload/", views.upload_image,name="upload api"),
    path('image-list/', views.image_list, name='image_list'),
    path("",views.index,name="index")
]
    