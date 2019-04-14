from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include



urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('',include('pages.urls')),
    path('',include('contacts.urls')),
    path('listings/',include('listings.urls')),
    path('realtors/', include('realtors.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
