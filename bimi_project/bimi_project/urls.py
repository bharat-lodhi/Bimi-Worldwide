from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from django.views.static import serve # Ye zaroori hai
from django.urls import re_path # Ye bhi zaroori hai

urlpatterns = [
    path('',include('website.urls')),
    path('bimi-admin/', include('custom_admin.urls')),
]
# Ye block add karein
if not settings.DEBUG:
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    ]
    
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)