# Task Management

This is a Django RESTful API-based Task Management application that allows users to register, log in, and manage tasks.
Users can perform CRUD operations on tasks. The project is containerized using Docker for easy setup and deployment.

## Features

- User registration and authentication (JWT-based login).
- Task management with the ability to Create, Read, Update, and Delete tasks.
- Fully tested with Django's testing framework.
- Dockerized for simplified deployment.
- **Swagger API documentation** for easy interaction with the API.

## Requirements

- Python 3.12+
- Django 5.x
- Django REST Framework
- Docker
- Docker Compose

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/darkkLUCIFER/sanaap_task.git
cd sanaap_task
```

### 2. Build the Docker containers

```bash
docker-compose up -d --build
```

This will run the application on http://localhost:8000.

### 3. Create a superuser (optional)

```bash
docker-compose exec api python manage.py createsuperuser
```
the phone should start with 98
### 4. Run Tests

You can run tests for both the accounts and tasks apps using the following command:

```bash
docker-compose exec api python manage.py test
```

### 5. Accessing the Application

The application will be available at:

- API Root: http://localhost:8000/
- Django Admin: http://localhost:8000/admin/
- Swagger Documentation: http://localhost:8000/swagger/

### 6. API Endpoints

Authentication

- POST /api/accounts/register/ - Register a new user.
- POST /api/accounts/login/ - Login and obtain JWT token.

Tasks

- GET /api/tasks/ - Retrieve all tasks.
- POST /api/tasks/ - Create a new task.
- GET /api/tasks/<id>/ - Retrieve a single task by ID.
- PUT /api/tasks/<id>/ - Update a task by ID.
- DELETE /api/tasks/<id>/ - Delete a task by ID.

