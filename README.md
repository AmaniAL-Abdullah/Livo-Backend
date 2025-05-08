# Livo Backend

**Livo Backend** is the server-side part of the Livo web application, providing robust RESTful APIs to manage **roles**, **tasks**, and **achievements**. It is built using **Django** and **Django REST Framework** with **PostgreSQL** as the database. This backend is designed to handle user authentication, data persistence, and interactions between roles, tasks, and achievements in a secure and efficient manner.

----

## Tech Stack

- **Django** — A high-level Python web framework for rapid development.
- **Django REST Framework** — Toolkit for building Web APIs in Django.
- **PostgreSQL** — A powerful, open-source relational database system.
- **JWT (JSON Web Token)** — Authentication mechanism for secure communication.
- **Python** — Programming language used to write the backend application.
- **Docker** — Containerization platform to ensure consistent development and production environments.

----

## Front End Repository

You can find the frontend repository here:  
[Frontend Repo](https://git.generalassemb.ly/amani/livo-frontend)

----

## ERD (Entity Relationship Diagram)

![ERD](assets/ERD.jpeg)

----
## Routing Table

Below is the routing table for the backend API:

### Role Endpoints:

| Method  | Endpoint               | Description                                      |
|---------|------------------------|--------------------------------------------------|
| **GET** | `/roles/`              | Retrieve all roles for the authenticated user.   |
| **POST**| `/roles/`              | Create a new role for the authenticated user.    |
| **GET** | `/roles/<int:pk>/`      | Retrieve details of a specific role.             |
| **PATCH**| `/roles/<int:pk>/`     | Update a specific role.                          |
| **DELETE**| `/roles/<int:pk>/`    | Delete a specific role.                          |

### Task Endpoints:

| Method  | Endpoint                | Description                                       |
|---------|-------------------------|---------------------------------------------------|
| **GET** | `/tasks/`               | Retrieve all tasks for the authenticated user.    |
| **POST**| `/tasks/`               | Create a new task for the authenticated user.     |
| **GET** | `/roles/<int:pk>/tasks/`| Retrieve all tasks for a specific role.           |
| **GET** | `/task/<int:pk>/`       | Retrieve the details of a specific task.          |
| **PATCH**| `/task/<int:pk>/`      | Update a specific task.                           |
| **DELETE**| `/task/<int:pk>/`     | Delete a specific task.                           |

### Achievement Endpoints:

| Method  | Endpoint                  | Description                                          |
|---------|---------------------------|------------------------------------------------------|
| **GET** | `/roles/<int:pk>/achievements/` | Retrieve all achievements for a specific role.     |
| **POST**| `/achievements/`          | Create a new achievement for the authenticated user. |
| **GET** | `/achievement/<int:pk>/`  | Retrieve the details of a specific achievement.      |
| **PATCH**| `/achievement/<int:pk>/` | Update a specific achievement.                       |
| **DELETE**| `/achievement/<int:pk>/`| Delete a specific achievement.                       |

### Authentication Endpoints:

| Method  | Endpoint                 | Description                                      |
|---------|--------------------------|--------------------------------------------------|
| **POST**| `/token/`                | Obtain a JWT token pair for the user.            |
| **POST**| `/token/refresh/`        | Refresh the JWT token pair.                      |
| **POST**| `/signup/`               | Create a new user and return a JWT token pair.   |
---

## Installation Instructions

### 1. Clone the Repository


git clone https://git.generalassemb.ly/amani/livo-backend.git
cd livo-backend
### 2\. Install Dependencies

Make sure you have **Python 3.x** installed. Then install the required dependencies using pip:


`pip install -r requirements.txt`

### 3\. Set Up Database

Make sure **PostgreSQL** is installed and running. Create a database for the project:


`# In PostgreSQL shell CREATE DATABASE livo_db;`

### 4\. Apply Migrations

Run the migrations to set up the database schema:

`python manage.py migrate`

### 5\. Create Environment Variables

Create a `.env` file in the root of the project directory:


`touch .env`

Inside the `.env` file, add your **secret key**, **database credentials**, and **JWT settings**:

`SECRET_KEY=your_secret_key DATABASE_URL=postgres://user:password@localhost:5432/livo_db JWT_SECRET_KEY=your_jwt_secret_key`

### 6\. Start the Development Server

Run the development server:

`python manage.py runserver`

----

## IceBox Features

*   Calendar integration for task deadlines     
*   Drag-and-drop interface for reordering tasks    
*   Dark mode theme toggle    
*   Notifications for upcoming tasks or achievements    
*   Ability to share roles with other users
