# Todo API - Django REST Framework

A secure Todo API built using Django REST Framework where users can manage their personal tasks with token-based authentication.

## Live Demo

Swagger Documentation:

```bash
http://15.206.79.170/swagger/
```

---

# Features

- User Authentication using Token Authentication
- User Authorization
- CRUD operations for tasks
- API documentation using Swagger
- AWS EC2 Deployment
- Generic Views implementation
- Secure task ownership filtering

---

# Tech Stack

- Python
- Django
- Django REST Framework
- DRF Token Authentication
- Swagger (drf-yasg)
- SQLite
- AWS EC2
- Gunicorn
- Nginx
- Git/GitHub

---

# Project Structure

```bash
todo-do/
│
├── todo/
├── todoproject/
├── manage.py
├── requirements.txt
├── db.sqlite3
└── README.md
```

---

# API Endpoints

## Token Authentication

Generate Token:

```bash
POST /token/
```

Example Response:

```json
{
    "token": "your_generated_token"
}
```

Use token in headers:

```bash
Authorization: Token your_generated_token
```

---

# Task Endpoints

## Get All Tasks

```bash
GET /tasks/
```

---

## Create Task

```bash
POST /tasks/
```

Example Request:

```json
{
    "title": "Complete Django project"
}
```

---

## Get Single Task

```bash
GET /tasks/{id}/
```

---

## Update Task

```bash
PUT /tasks/{id}/
```

---

## Partial Update Task

```bash
PATCH /tasks/{id}/
```

---

## Delete Task

```bash
DELETE /tasks/{id}/
```

---

# Authentication & Authorization

This project ensures users only access their own tasks.

Implemented using:

```python
def get_queryset(self):
    return Task.objects.filter(user=self.request.user)
```

Task ownership is automatically assigned:

```python
def perform_create(self, serializer):
    serializer.save(user=self.request.user)
```

---

# Generic Views Used

- ListCreateAPIView
- RetrieveUpdateDestroyAPIView

These reduce boilerplate and simplify CRUD operations.

---

# Swagger Documentation

Swagger UI integrated using:

```bash
drf-yasg
```

Access Swagger:

```bash
http://15.206.79.170/swagger/
```

---

# Local Setup

Clone repository:

```bash
git clone https://github.com/yourusername/todo-do.git
```

Move into project:

```bash
cd todo-do
```

Create virtual environment:

```bash
python3 -m venv env
```

Activate environment:

```bash
source env/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py migrate
```

Run server:

```bash
python manage.py runserver
```

---

# Deployment Process

Deployed on :contentReference[oaicite:0]{index=0} EC2 using:

- Ubuntu Server
- Gunicorn
- Nginx Reverse Proxy
- Security Group Configuration
- GitHub Deployment

Run production server:

```bash
gunicorn todoproject.wsgi:application --bind 0.0.0.0:8000
```

---

# Git Commands Used

Initialize git:

```bash
git init
```

Add files:

```bash
git add .
```

Commit:

```bash
git commit -m "Initial commit"
```

Create branch:

```bash
git branch -M main
```

Connect GitHub repo:

```bash
git remote add origin https://github.com/yourusername/todo-do.git
```

Push code:

```bash
git push -u origin main
```

---

# .gitignore

```bash
env/
__pycache__/
db.sqlite3
.env
*.pyc
```

---

# Future Improvements

- PostgreSQL integration
- JWT authentication
- Docker deployment
- CI/CD pipeline
- HTTPS setup
- Role-based access

---

# Author

**Muhammed Dhanish K**

AI/ML Engineer | Data Analyst | Statistics Graduate
