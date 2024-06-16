from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.urls import path
from rest_framework_swagger.views import get_swagger_view
from django.urls import re_path as url


schema_view = get_swagger_view(title='Pastebin API')
urlpatterns = [
    url(r'^$', schema_view),
    path('admin/', admin.site.urls),
    path('api/', include('ocr.urls')),
    path('api/', include('gpt.urls')),
    path('api/', include('paraphraser.urls')),
    path('api/', include('handwriting.urls'))
]
