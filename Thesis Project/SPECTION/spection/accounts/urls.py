
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # User Panel
    path('', views.home, name='home'),
     path('Services/', views.services, name='services'),
    path('calendar/', views.calendar, name='calendar'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('post/', views.post, name='post'),
    path('patient/', views.patient, name='patient'),
    path('patient/Order/<str:pk>/Details', views.patientOrderDetails, name="view_patient_order"),
    # Admin Panel
    path('registration/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('appointment/', views.appointment, name='appointment'),
    path('Billing/', views.billing, name='billing'),
    path('dues/', views.dues, name='dues'),
    path('news/', views.news, name='news'),
    path('schedule/', views.schedule, name='schedule'),
    path('products/', views.products, name='products'),
    # Patient
    path('patient_list/', views.patient_list, name='patient list'),
    path('delete_patient/<str:pk>', views.deletePatient, name="delete_patient"),

    # Patient Sidebar
    path('patient_list/patient/<str:pk>/Information/',
         views.person_info, name='person_info'),
    path('patient_list/patient/<str:pk>/Information/update/',
         views.update_info, name='update_info'),

    path('patient_list/patient/<str:pk>/Case/',
         views.person_list_case, name='person_list_case'),
    path('patient_list/patient/<str:pk>/RX/',
         views.person_list_rx, name='person_list_rx'),
    path('patient_list/patient/<str:pk>/RX/<str:rx_id>/update/',
         views.update_rx, name='update_rx'),
    path('patient_list/patient/<str:pk>/RX/<str:rx_id>/delete/',
         views.delete_rx, name='delete_rx'),
    # Patient RX
    path('patient_list/patient/<str:pk>/RX/create',
         views.create_rx, name='create_rx'),
    # Patient Case
    path('patient_list/patient/<str:pk>/Case/create_case/',
         views.create_case, name='create_case'),
    path('patient_list/patient/<str:pk>/Case/<str:case_id>/',
         views.person_case, name='person_case'),
    path('patient_list/patient/<str:pk>/Case/<str:case_id>/update/',
         views.update_case, name='update_case'),
    path('patient_list/patient/<str:pk>/Case/<str:case_id>/delete_case/',
         views.delete_case, name='delete_case'),
     # Appointment
     path('Appointment/Create', views.create_appointment, name='create_appointment'),
     path('Appointment/<str:pk>/Delete', views.delete_appointment, name='delete_appointment'),
    # Billing
    path('Billing/Create', views.create_billing, name='create_billing'),
    # Schedule
    path('Schedule/Create/', views.create_schedule, name="create_schedule"),
    path('Schedule/<str:pk>/Update', views.update_schedule, name="update_schedule"),
    path('Schedule/<str:pk>/Delete', views.delete_schedule, name="delete_schedule"),
    # News
    path('News/Create/', views.create_news, name="create_news"),
    path('News/<str:pk>/update/', views.update_news, name="update_news"),
    path('News/<str:pk>/delete/', views.delete_news, name="delete_news"),
    # Order
    path('orders/', views.orders, name='orders'),
    path('create_order/', views.create_order, name='create_order'),
     path('View Order/<str:pk>', views.viewOrder, name="view_order"),
    path('update_order/<str:pk>', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>', views.deleteOrder, name="delete_order"),
    # Reset Passwords
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="accounts/pages/forgot_password.html"),
         name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="accounts/pages/password_reset_sent.html"),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/pages/password_reset_confirm.html"),
         name="password_reset_confirm"),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="accounts/pages/password_reset_complete.html"), name="password_reset_complete"),
]
