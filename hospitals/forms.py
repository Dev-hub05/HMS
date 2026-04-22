from django import forms
from .models import Doctor, Patient, Appointment, Contact


class DoctorForm(forms.ModelForm):
    """Form for creating and editing Doctor records."""

    class Meta:
        model = Doctor
        fields = ['name', 'phone', 'specialization', 'email']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'e.g., John Smith',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'e.g., +91 9876543210',
            }),
            'specialization': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'e.g., Cardiology',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'e.g., doctor@hospital.com',
            }),
        }
        labels = {
            'name': 'Full Name',
            'phone': 'Phone Number',
            'specialization': 'Specialization',
            'email': 'Email Address',
        }


class PatientForm(forms.ModelForm):
    """Form for creating and editing Patient records."""

    class Meta:
        model = Patient
        fields = ['name', 'gender', 'phone', 'date_of_birth', 'address']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'e.g., Jane Doe',
            }),
            'gender': forms.Select(attrs={
                'class': 'form-select',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'e.g., +91 9876543210',
            }),
            'date_of_birth': forms.DateInput(attrs={
                'class': 'form-input',
                'type': 'date',
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-textarea',
                'placeholder': 'Full address',
                'rows': 3,
            }),
        }
        labels = {
            'name': 'Full Name',
            'gender': 'Gender',
            'phone': 'Phone Number',
            'date_of_birth': 'Date of Birth',
            'address': 'Address',
        }


class AppointmentForm(forms.ModelForm):
    """Form for creating and editing Appointment records."""

    class Meta:
        model = Appointment
        fields = ['doctor', 'patient', 'date', 'time', 'status', 'notes']
        widgets = {
            'doctor': forms.Select(attrs={
                'class': 'form-select',
            }),
            'patient': forms.Select(attrs={
                'class': 'form-select',
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-input',
                'type': 'date',
            }),
            'time': forms.TimeInput(attrs={
                'class': 'form-input',
                'type': 'time',
            }),
            'status': forms.Select(attrs={
                'class': 'form-select',
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-textarea',
                'placeholder': 'Any additional notes...',
                'rows': 3,
            }),
        }


class ContactForm(forms.ModelForm):
    """Public contact form for visitors."""

    class Meta:
        model = Contact
        fields = ['name', 'phone', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Your full name',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Your phone number',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'your@email.com',
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'What is this regarding?',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-textarea',
                'placeholder': 'Write your message here...',
                'rows': 5,
            }),
        }
