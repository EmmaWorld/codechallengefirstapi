# codechallengefirstapi

FastAPI Student API
This is a simple API built using FastAPI to manage student data. It allows you to perform CRUD operations on book objects.

Installation
Clone the repository: bash Copy code git clone <repository_url> Install the dependencies using pip: Copy code pip install -r requirements.txt Run the application: css Copy code uvicorn student:app --reload The API will be available at http://localhost:8000.

Endpoints
GET / Returns a list of all students.

GET /student/{student_id} Returns details of a specific student identified by {id}.

PATCH /students/{student_id} Updates the details of a specific student identified by {id}.

DELETE /students/{student_id} Deletes a specific student identified by {id}.

POST /students Adds a new student to the database.
