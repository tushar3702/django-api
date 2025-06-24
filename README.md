# 🎯 Student Management REST API

🎯 A clean and scalable RESTful API built using **Django** and **Django REST Framework (DRF)** to perform CRUD operations on student records. Ideal for learning or as a backend template.

---

## 🎯 Tech Stack

- 🎯 Python 3.12
- 🎯 Django 5.1
- 🎯 Django REST Framework
- 🎯 SQLite (default)
- 🎯 Postman (for API testing)

---

## 🎯 Features

- 🎯 Create, Read, Update, and Delete student records
- 🎯 ModelSerializer for automatic JSON serialization
- 🎯 Class-based views using `ModelViewSet`
- 🎯 DRF `DefaultRouter` for clean URL routing
- 🎯 Browsable API for testing
- 🎯 Scalable app structure

---

## 🎯 Project Structure
django-api/
│
├── students/ # Student app
│ ├── models.py
│ ├── serializers.py
│ ├── views.py
│ └── urls.py
│
├── student_api/ # Project settings
│ ├── settings.py
│ └── urls.py
│
├── db.sqlite3 # Database
├── manage.py
