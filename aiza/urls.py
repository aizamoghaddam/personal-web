from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('about/', include('about.urls')),
    path('work/', include('work.urls')),
    path('contact/', include('contact.urls'))
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
