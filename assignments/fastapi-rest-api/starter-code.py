# FastAPI Task Management API - Starter Code

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

# Create FastAPI application instance
app = FastAPI()

# TODO: Define a Pydantic model for Task
# Hint: Include fields for id, title, description, and completed status
class Task(BaseModel):
    pass  # Replace 'pass' with your field definitions


# TODO: Define a Pydantic model for creating new tasks (without id)
class TaskCreate(BaseModel):
    pass  # Replace 'pass' with your field definitions


# In-memory storage for tasks
tasks = []
task_id_counter = 1


# TODO: Task 1 - Create root endpoint
@app.get("/")
def read_root():
    # Return a welcome message as JSON
    pass


# TODO: Task 1 - Create info endpoint
@app.get("/info")
def get_info():
    # Return API metadata (name, version, description)
    pass


# TODO: Task 2 - Get all tasks
@app.get("/tasks")
def get_tasks():
    # Return the list of all tasks
    pass


# TODO: Task 2 - Create a new task
@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):
    # Add a new task to the tasks list
    # Remember to assign an id and increment the counter
    pass


# TODO: Task 2 - Get a specific task by ID
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    # Find and return the task with the given id
    # If not found, raise HTTPException with status_code 404
    pass


# TODO: Task 2 - Update a task by ID
@app.put("/tasks/{task_id}")
def update_task(task_id: int, task_update: TaskCreate):
    # Find the task and update its properties
    # If not found, raise HTTPException with status_code 404
    pass


# TODO: Task 2 - Delete a task by ID
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    # Remove the task from the list
    # If not found, raise HTTPException with status_code 404
    pass


# Run the application with: uvicorn starter-code:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
