from django.urls import path
from organizer import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('add/', views.add_organizer),
    path('dashboard/', views.dashboard),
    path('delete/<id>', views.delete_booking),
    
]


