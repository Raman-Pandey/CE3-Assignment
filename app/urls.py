from django.urls import path
from .views import UploadFile

urlpatterns = [
    path('UploadFile', UploadFile, name='upload'),
]
