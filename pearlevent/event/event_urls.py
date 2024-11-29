from django.urls import path
from event import views

urlpatterns = [
    path('', views.show_event),
    path('add/', views.add_event),
    path('delete/<id>', views.delete_event),
    path('update/<id>', views.update_event),

        
]
from django.conf.urls.static import static
from django.conf import settings
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)