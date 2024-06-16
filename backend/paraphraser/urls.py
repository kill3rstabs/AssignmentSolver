# paraphraser/urls.py

from django.urls import path
from .views import ParaphraseView

urlpatterns = [
    path('paraphrase', ParaphraseView.as_view(), name='paraphrase'),
]
