from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('customer.customer_urls')),
    path('organizer/', include('organizer.organizer_urls')),
    path('event/', include('event.event_urls')),

]
from django.conf.urls.static import static
from django.conf import settings
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)