from django.contrib import admin
from .models import Doctor, Patient, Appointment, Contact


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'specialization', 'email', 'created_at']
    search_fields = ['name', 'specialization', 'email']
    list_per_page = 20


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['name', 'gender', 'phone', 'address', 'created_at']
    search_fields = ['name', 'phone']
    list_filter = ['gender']
    list_per_page = 20


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['doctor', 'patient', 'date', 'time', 'status', 'created_at']
    search_fields = ['doctor__name', 'patient__name']
    list_filter = ['status', 'date']
    list_per_page = 20


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'is_read', 'created_at']
    search_fields = ['name', 'email', 'subject']
    list_filter = ['is_read']
    list_per_page = 20
