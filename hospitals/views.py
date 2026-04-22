from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from datetime import date

from .models import Doctor, Patient, Appointment, Contact
from .forms import DoctorForm, PatientForm, AppointmentForm, ContactForm


def staff_required(view_func):
    """Decorator that requires user to be authenticated staff."""
    decorated = login_required(login_url='login')(
        user_passes_test(lambda u: u.is_staff, login_url='login')(view_func)
    )
    return decorated


# ═══════════════════════════════════════════════════════════
# PUBLIC VIEWS
# ═══════════════════════════════════════════════════════════

def index(request):
    """Public landing page with hospital stats."""
    context = {
        'doctor_count': Doctor.objects.count(),
        'patient_count': Patient.objects.count(),
        'appointment_count': Appointment.objects.count(),
    }
    return render(request, 'index.html', context)


def about(request):
    """Public about page."""
    return render(request, 'about.html')


def contact(request):
    """Public contact form."""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully! We will get back to you soon.')
            return redirect('contact')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


# ═══════════════════════════════════════════════════════════
# AUTHENTICATION
# ═══════════════════════════════════════════════════════════

def admin_login(request):
    """Admin login page."""
    if request.user.is_authenticated and request.user.is_staff:
        return redirect('dashboard')

    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_staff:
            login(request, user)
            messages.success(request, f'Welcome back, {user.get_full_name() or user.username}!')
            next_url = request.GET.get('next', 'dashboard')
            return redirect(next_url)
        else:
            messages.error(request, 'Invalid credentials or insufficient permissions.')

    return render(request, 'login.html')


def admin_logout(request):
    """Log out and redirect to home."""
    logout(request)
    messages.info(request, 'You have been logged out successfully.')
    return redirect('index')


# ═══════════════════════════════════════════════════════════
# DASHBOARD
# ═══════════════════════════════════════════════════════════

@staff_required
def dashboard(request):
    """Admin dashboard with statistics and recent activity."""
    today = date.today()

    context = {
        'doctor_count': Doctor.objects.count(),
        'patient_count': Patient.objects.count(),
        'appointment_count': Appointment.objects.count(),
        'query_count': Contact.objects.filter(is_read=False).count(),
        'today_appointments': Appointment.objects.filter(date=today).select_related('doctor', 'patient')[:10],
        'recent_patients': Patient.objects.all()[:5],
        'recent_queries': Contact.objects.filter(is_read=False)[:5],
        # Chart data
        'pending_count': Appointment.objects.filter(status='Pending').count(),
        'confirmed_count': Appointment.objects.filter(status='Confirmed').count(),
        'completed_count': Appointment.objects.filter(status='Completed').count(),
        'cancelled_count': Appointment.objects.filter(status='Cancelled').count(),
    }
    return render(request, 'dashboard.html', context)


# ═══════════════════════════════════════════════════════════
# DOCTOR MANAGEMENT
# ═══════════════════════════════════════════════════════════

@staff_required
def doctor_list(request):
    """List all doctors with search and pagination."""
    query = request.GET.get('q', '')
    doctors = Doctor.objects.all()

    if query:
        doctors = doctors.filter(
            Q(name__icontains=query) | Q(specialization__icontains=query) | Q(email__icontains=query)
        )

    paginator = Paginator(doctors, 10)
    page = request.GET.get('page')
    doctors = paginator.get_page(page)

    return render(request, 'doctor_list.html', {'doctors': doctors, 'query': query})


@staff_required
def doctor_form(request, pk=None):
    """Add or edit a doctor."""
    doctor = get_object_or_404(Doctor, pk=pk) if pk else None

    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            action = 'updated' if pk else 'added'
            messages.success(request, f'Doctor {action} successfully!')
            return redirect('doctor_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = DoctorForm(instance=doctor)

    context = {
        'form': form,
        'doctor': doctor,
        'is_edit': pk is not None,
    }
    return render(request, 'doctor_form.html', context)


@staff_required
def doctor_delete(request, pk):
    """Delete a doctor (POST only)."""
    if request.method == 'POST':
        doctor = get_object_or_404(Doctor, pk=pk)
        doctor.delete()
        messages.success(request, 'Doctor deleted successfully!')
    return redirect('doctor_list')


# ═══════════════════════════════════════════════════════════
# PATIENT MANAGEMENT
# ═══════════════════════════════════════════════════════════

@staff_required
def patient_list(request):
    """List all patients with search and pagination."""
    query = request.GET.get('q', '')
    patients = Patient.objects.all()

    if query:
        patients = patients.filter(
            Q(name__icontains=query) | Q(phone__icontains=query) | Q(address__icontains=query)
        )

    paginator = Paginator(patients, 10)
    page = request.GET.get('page')
    patients = paginator.get_page(page)

    return render(request, 'patient_list.html', {'patients': patients, 'query': query})


@staff_required
def patient_form(request, pk=None):
    """Add or edit a patient."""
    patient = get_object_or_404(Patient, pk=pk) if pk else None

    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            action = 'updated' if pk else 'added'
            messages.success(request, f'Patient {action} successfully!')
            return redirect('patient_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = PatientForm(instance=patient)

    context = {
        'form': form,
        'patient': patient,
        'is_edit': pk is not None,
    }
    return render(request, 'patient_form.html', context)


@staff_required
def patient_delete(request, pk):
    """Delete a patient (POST only)."""
    if request.method == 'POST':
        patient = get_object_or_404(Patient, pk=pk)
        patient.delete()
        messages.success(request, 'Patient deleted successfully!')
    return redirect('patient_list')


# ═══════════════════════════════════════════════════════════
# APPOINTMENT MANAGEMENT
# ═══════════════════════════════════════════════════════════

@staff_required
def appointment_list(request):
    """List all appointments with search, filter, and pagination."""
    query = request.GET.get('q', '')
    status_filter = request.GET.get('status', '')
    appointments = Appointment.objects.select_related('doctor', 'patient')

    if query:
        appointments = appointments.filter(
            Q(doctor__name__icontains=query) | Q(patient__name__icontains=query)
        )

    if status_filter:
        appointments = appointments.filter(status=status_filter)

    paginator = Paginator(appointments, 10)
    page = request.GET.get('page')
    appointments = paginator.get_page(page)

    context = {
        'appointments': appointments,
        'query': query,
        'status_filter': status_filter,
        'status_choices': Appointment.STATUS_CHOICES,
    }
    return render(request, 'appointment_list.html', context)


@staff_required
def appointment_form(request, pk=None):
    """Add or edit an appointment."""
    appointment = get_object_or_404(Appointment, pk=pk) if pk else None

    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            action = 'updated' if pk else 'scheduled'
            messages.success(request, f'Appointment {action} successfully!')
            return redirect('appointment_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = AppointmentForm(instance=appointment)

    context = {
        'form': form,
        'appointment': appointment,
        'is_edit': pk is not None,
    }
    return render(request, 'appointment_form.html', context)


@staff_required
def appointment_delete(request, pk):
    """Delete an appointment (POST only)."""
    if request.method == 'POST':
        appointment = get_object_or_404(Appointment, pk=pk)
        appointment.delete()
        messages.success(request, 'Appointment deleted successfully!')
    return redirect('appointment_list')


# ═══════════════════════════════════════════════════════════
# QUERY / CONTACT MANAGEMENT
# ═══════════════════════════════════════════════════════════

@staff_required
def query_list(request):
    """List contact queries with filter tabs (all / unread / read)."""
    filter_type = request.GET.get('filter', 'all')
    contacts = Contact.objects.all()

    if filter_type == 'unread':
        contacts = contacts.filter(is_read=False)
    elif filter_type == 'read':
        contacts = contacts.filter(is_read=True)

    paginator = Paginator(contacts, 10)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)

    context = {
        'contacts': contacts,
        'filter_type': filter_type,
    }
    return render(request, 'query_list.html', context)


@staff_required
def query_detail(request, pk):
    """View a single query and mark it as read."""
    query = get_object_or_404(Contact, pk=pk)

    if not query.is_read:
        query.is_read = True
        query.save(update_fields=['is_read'])

    return render(request, 'query_detail.html', {'query': query})


@staff_required
def query_delete(request, pk):
    """Delete a query (POST only)."""
    if request.method == 'POST':
        query = get_object_or_404(Contact, pk=pk)
        query.delete()
        messages.success(request, 'Query deleted successfully!')
    return redirect('query_list')
