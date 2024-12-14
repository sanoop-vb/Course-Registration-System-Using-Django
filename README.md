# Course Registration System

A web-based course registration system built with Django for the backend and HTML/CSS for the frontend. This system allows users to view available courses, register for them, and manage their enrollment. 

## Features

- **Course Listing**: View a list of available courses with descriptions, available slots, and enrolled students.
- **Course Registration**: Register for courses based on availability.
- **Responsive Design**: The application is fully responsive, meaning it works on all screen sizes.
- **Student Management**: Students can be registered, and enrollment is tracked for each course.

## Technologies Used

- **Backend**: Django
- **Frontend**: HTML, CSS (for responsive design)
- **Database**: SQLite (default, can be configured to use others like PostgreSQL or MySQL)

## Requirements

- Python 3.x
- Django 3.x or above

## Installation

Follow these steps to get your local development environment running:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/course-registration.git
    cd course-registration
    ```

2. **Set up a virtual environment**:
    - Create a virtual environment:
      ```bash
      python -m venv env
      ```
    - Activate the virtual environment:
        - **Windows**:
          ```bash
          env\Scripts\activate
          ```
        - **Mac/Linux**:
          ```bash
          source env/bin/activate
          ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

6. **Visit the app**:
    Open your browser and go to `http://127.0.0.1:8000/` to see the application in action.



