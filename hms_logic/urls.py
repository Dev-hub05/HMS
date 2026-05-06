from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views, api_views

router = DefaultRouter()
router.register(r'doctors', api_views.DoctorViewSet)
router.register(r'patients', api_views.PatientViewSet)
router.register(r'appointments', api_views.AppointmentViewSet)

urlpatterns = [
    # ── Public Pages ──
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    # ── Authentication ──
    path('login/', views.admin_login, name='login'),
    path('logout/', views.admin_logout, name='logout'),

    # ── Admin Dashboard ──
    path('dashboard/', views.dashboard, name='dashboard'),

    # ── Doctor Management ──
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('doctors/add/', views.doctor_form, name='doctor_add'),
    path('doctors/<int:pk>/edit/', views.doctor_form, name='doctor_edit'),
    path('doctors/<int:pk>/delete/', views.doctor_delete, name='doctor_delete'),

    # ── Patient Management ──
    path('patients/', views.patient_list, name='patient_list'),
    path('patients/add/', views.patient_form, name='patient_add'),
    path('patients/<int:pk>/edit/', views.patient_form, name='patient_edit'),
    path('patients/<int:pk>/delete/', views.patient_delete, name='patient_delete'),

    # ── Appointment Management ──
    path('appointments/', views.appointment_list, name='appointment_list'),
    path('appointments/add/', views.appointment_form, name='appointment_add'),
    path('appointments/<int:pk>/edit/', views.appointment_form, name='appointment_edit'),
    path('appointments/<int:pk>/delete/', views.appointment_delete, name='appointment_delete'),

    # ── Query / Contact Management ──
    path('queries/', views.query_list, name='query_list'),
    path('queries/<int:pk>/', views.query_detail, name='query_detail'),
    path('queries/<int:pk>/delete/', views.query_delete, name='query_delete'),

    # ── API Endpoints ──
    path('api/', include(router.urls)),
]
