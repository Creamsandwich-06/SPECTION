from django.urls import path
from . import views

urlpatterns = [
    # User Panel
    path('', views.home, name='home'),
    path('calendar/', views.calendar, name='calendar'),
    path('login/', views.login, name='login'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('patient/<str:pk>/', views.patient, name='patient'),
    # Admin Panel
    path('registration/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('products/', views.products, name='products'),
    path('patient list/', views.patient_list, name='patient list'),
    # Order
    path('orders/', views.orders, name='orders'),

    path('create order/', views.BookCreateView.as_view(), name='create_order'),

]
