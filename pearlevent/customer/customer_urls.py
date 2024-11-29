from django.urls import path
from customer import views
urlpatterns = [
    path('', views.home),
    path('register/', views.register),
    path('login/', views.customer_login),
    path('logout/', views.customer_logout),
    path('service/', views.service),
    path('book-event/<id>', views.book_event),
    path('search/', views.search_event),
    # path('customer-details/', views.customer_details),
    # path('create/',  views.customer_create),
    # path('update /', views.customer_update),
    # path('delete /', views.customer_delete),
        
]
