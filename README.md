# 🏥 Hospital Management System (HMS)

[![Django](https://img.shields.io/badge/Framework-Django%203.2-092e20?style=for-the-badge&logo=django)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Language-Python%203.x-3776ab?style=for-the-badge&logo=python)](https://www.python.org/)
[![DRF](https://img.shields.io/badge/API-Django%20Rest%20Framework-ff1709?style=for-the-badge&logo=django)](https://www.django-rest-framework.org/)
[![Database](https://img.shields.io/badge/Database-SQLite-003b57?style=for-the-badge&logo=sqlite)](https://www.sqlite.org/)

A professional, full-stack Hospital Management System designed to streamline medical workflows, patient record keeping, and appointment scheduling. Built with a focus on high-performance, responsive UI, and secure data handling.

---

## 🚀 Key Features

### 👨‍⚕️ Doctor Management
*   **Comprehensive Profiles**: Manage doctor details including specializations and contact info.
*   **Search & Filter**: Quickly find doctors by name, specialization, or email.
*   **Seamless CRUD**: Add, edit, and manage the hospital's medical staff with ease.

### 👥 Patient Care
*   **Electronic Health Records (EHR)**: Securely store patient personal details and medical history.
*   **Intuitive Interface**: Simplified patient registration and record management.
*   **Searchable Records**: Instant access to patient data via optimized search queries.

### 📅 Advanced Appointment System
*   **Smart Scheduling**: Book appointments between patients and doctors with specific time slots.
*   **Status Tracking**: Manage life-cycle of appointments (Pending → Confirmed → Completed → Cancelled).
*   **Automated Dashboards**: Real-time overview of today's schedule and upcoming visits.

### 📩 Inquiry & Query Management
*   **Public Contact Portal**: Integrated contact form for public inquiries.
*   **Admin Query Hub**: Dedicated interface for hospital staff to manage and respond to messages.
*   **Read/Unread Tracking**: Visual indicators for pending queries.

### 🔌 RESTful API Integration
*   Full API support for external integrations using **Django Rest Framework**.
*   Standardized JSON responses for Doctors, Patients, and Appointments.

---

## 🎨 UX & Design Philosophy

The HMS is engineered with a **User-First** approach, ensuring that medical staff can focus on care rather than software complexity.

*   **Modern Dashboard**: A centralized hub featuring real-time statistics cards and activity feeds.
*   **Responsive Layout**: Fully functional on desktops, tablets, and mobile devices.
*   **Visual Cues**: Extensive use of status-aware color coding (e.g., Green for Confirmed, Yellow for Pending, Red for Cancelled).
*   **Glassmorphism & Minimalism**: Sleek, non-intrusive design elements with a focus on readability and accessibility.

---

## 🛠️ Technology Stack

| Layer | Technology |
| :--- | :--- |
| **Backend** | Python 3.x, Django 3.2 |
| **Frontend** | HTML5, CSS3, JavaScript, Django Templates |
| **API** | Django Rest Framework (DRF) |
| **Database** | SQLite3 (Production-ready with PostgreSQL support) |
| **Styling** | Vanilla CSS (Custom System), Google Fonts (Inter/Outfit) |

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Dev-hub05/HospitalManagementSystem.git
cd HospitalManagementSystem
```

### 2. Set Up Virtual Environment
```bash
python -m venv venv
# Windows
.\venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Admin)
```bash
python manage.py createsuperuser
```

### 6. Run the Server
```bash
python manage.py run_server
```
Visit `http://127.0.0.1:8000/` to view the landing page or `/dashboard/` for the admin portal.

---

## 🛣️ API Endpoints

The system exposes the following REST API endpoints for developers:

| Endpoint | Method | Description |
| :--- | :--- | :--- |
| `/api/doctors/` | GET/POST | List and create doctors |
| `/api/patients/` | GET/POST | List and create patients |
| `/api/appointments/` | GET/POST | List and schedule appointments |

---

## 📄 License
Distributed under the MIT License. See `LICENSE` for more information.

## ✉️ Contact
**Project Maintainer**: [Dev-hub05](https://github.com/Dev-hub05)
**Project Link**: [https://github.com/Dev-hub05/HospitalManagementSystem](https://github.com/Dev-hub05/HospitalManagementSystem)

---
*Created with ❤️ by the Antigravity AI Team*
