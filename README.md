# Task Manager Django App

Welcome to the Task Manager Django App! 🚀

This mini project is created with love and care by [@sebaszap123-dev](https://github.com/sebaszap123-dev). It's designed to help you manage your tasks efficiently.

## Features

📝 **Task Management**: Create, update, and delete tasks.

✅ **Task Status**: Toggle the status of tasks between done and undone.

🔒 **Authentication**: Secure endpoints with JWT authentication.

## Setup

To run this Django app locally, follow these steps:

1. Clone the repository:
`git clone https://github.com/sebaszap123-dev/task-manager.git`

2. Navigate to the project directory:
 ```
  cd task-manager
 ```
3. Create a virtual environment:
 ```
  python -m venv venv
 ```

5. Activate the virtual environment:
- **Windows**:
  ```
  venv\Scripts\activate
  ```
- **MacOS / Linux**:
  ```
  source venv/bin/activate
  ```
5. Install dependencies:
 ```
 pip install -r requirements.txt
 ```

6. Apply migrations:
  ```
  python manage.py migrate
  ```

7. Create a superuser:
```
python manage.py createsuperuser
```
8. Run the development server:
  ```
  python manage.py runserver
  ```

9. Access the Django admin interface at `http://localhost:8000/admin/` or `http://127.0.0.1:8000/admin/` and login with the superuser credentials.

## Usage

Once the server is running, you can interact with the API using tools like [Postman](https://www.postman.com/) or [curl](https://curl.se/). Also you can use Swagger `http://localhost:8000/swagger/` for see all the endpoints.
### Endpoints

- **GET** `/tasks/`: Retrieve all tasks.
- **POST** `/tasks/`: Create a new task.
- **GET** `/tasks/{task_id}/`: Retrieve a specific task.
- **PATCH** `/tasks/{task_id}/`: Update a specific task.
- **POST** `/tasks/{task_id}/update-status/`: Toggle the status of a specific task.
- **POST** `/tasks/{task_id}/update-task/`: Update a specific task partially.

### Authentication

To access protected endpoints, include a valid JWT token in the request header:
```
Authorization: Token <your_token_here>
```
You can create a token for a user in `/users/v1/api-token-auth/` with the credentials of the user and authenticate a user in a frontend app with the headers that we talk above (also in postman).
You are free to create user (not super user) in the User endpoints using swagger POST method in `/users/v1/users/` or doing the same in Postman
 
## Contribution

This project is open to contributions! Feel free to submit issues or pull requests to help improve the Task Manager Django App.

Happy task managing! ✨📋
