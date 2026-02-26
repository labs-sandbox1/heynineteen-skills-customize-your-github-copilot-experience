# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build modern REST APIs using the FastAPI framework in Python. You will create a simple task management API that demonstrates core REST principles including CRUD operations (Create, Read, Update, Delete) and proper HTTP methods.

## 📝 Tasks

### 🛠️	Create a Basic FastAPI Application

#### Description
Set up a FastAPI application with basic endpoints. You'll create a simple API that returns a welcome message and provides basic information about your task management service.

#### Requirements
Completed program should:

- Import FastAPI and create an app instance
- Create a root endpoint (`/`) that returns a welcome message as JSON
- Create an `/info` endpoint that returns API metadata (name, version, description)
- Run the application using uvicorn when executed as the main module


### 🛠️	Implement Task Management Endpoints

#### Description
Build a complete task management system with endpoints to create, read, update, and delete tasks. Each task should have an ID, title, description, and completion status.

#### Requirements
Completed program should:

- Store tasks in a list or dictionary (in-memory storage is fine)
- Implement a `GET /tasks` endpoint to retrieve all tasks
- Implement a `POST /tasks` endpoint to create a new task
- Implement a `GET /tasks/{task_id}` endpoint to retrieve a specific task by ID
- Implement a `PUT /tasks/{task_id}` endpoint to update an existing task
- Implement a `DELETE /tasks/{task_id}` endpoint to remove a task
- Use Pydantic models to validate request and response data
- Return appropriate HTTP status codes (200, 201, 404, etc.)

**Example Input/Output:**

Creating a task:
```json
POST /tasks
{
  "title": "Complete FastAPI assignment",
  "description": "Build a REST API with CRUD operations",
  "completed": false
}
```

Response:
```json
{
  "id": 1,
  "title": "Complete FastAPI assignment",
  "description": "Build a REST API with CRUD operations",
  "completed": false
}
```
