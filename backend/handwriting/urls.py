# paraphraser/urls.py

from django.urls import path
from .views import HandwritingAPIView

urlpatterns = [
    path('handwriting', HandwritingAPIView.as_view(), name='handwriting_api'),
]
