# gpt/urls.py

from django.urls import path
from .views import ChatView

urlpatterns = [
    path('gpt', ChatView.as_view(), name='chat'),
]
