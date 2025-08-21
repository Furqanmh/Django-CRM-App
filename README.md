# Client Record Manager in Django

A simple Client Record Management web application built with Python and Django.

# Setup Instructions

**1. Create and activate a virtual environment**

    python -m venv venv
    
   * **On macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```
   * **On Windows:**
        ```bash
        ./venv/Scripts/activate
        ```
        
**2. Install dependencies from requirements.txt**

   ```bash
    pip install -r requirements.txt
   ```
   
**3. Run Database Migration**

   ```bash
    python manage.py makemigrations
    python manage.py migrate
   ```
   
**4. (Optional) Create an Admin User**

   ```bash
    python manage.py createsuperuser
   ```
   Provide a username and password

**5. Run the server**

   ```bash
    python manage.py runserver
   ```

# Frameworks and Dependencies

1. Python 3.12.0
2. Django 5.2.5
3. Django Crispy Forms 1.14.0
4. Bootstrap for front-end
