# Library Management System - Backend

This repository contains the backend implementation of a Library Management System, providing REST APIs for managing books, members, and user authentication.

## Table of Contents
1. [Scenario](#scenario)
2. [Backend Structure](#backend-structure)
3. [Database Structure](#database-structure)
4. [API Documentation](#api-documentation)
5. [Hosting Instructions](#hosting-instructions)
6. [Links](#links)
7. [Documentation](#documentation)

## Scenario

There are two roles in the system: LIBRARIAN and MEMBER. Users can sign up as LIBRARIAN or MEMBER, log in to get JWT access tokens, and perform various actions based on their roles.

### Librarian Actions:
- Add, update, and remove books.
- Add, update, view, and remove members.

### Member Actions:
- View, borrow, and return available books.
- Change book status to BORROWED when borrowed and AVAILABLE when returned.
- Delete own account.

## Backend Structure

The backend is implemented using Django Rest Framework. The project structure includes:
- `/src`: Source code for the backend.
- `/config`: Configuration files.
- `/database`: Database scripts and migrations.
- `/docs`: API documentation.

## Database Structure

The database includes tables for User, Book. Below is a simplified representation:

**User Table:**
- user_id (Primary Key)
- username
- password
- issuperuser

**Book Table:**
- book_id (Primary Key)
- user (Foreign Key)
- title
- author
- status

## API Documentation

Detailed API documentation can be found in the `/docs` directory. It includes information on each endpoint, required input, expected output, and possible errors.

## Hosting Instructions

1. **Backend:**
This guide will walk you through the process of hosting the backend of the library management system on PythonAnywhere.

    **Steps:**

   **1. Create a PythonAnywhere Account**

   If you don't have a PythonAnywhere account, sign up for one at [PythonAnywhere](https://www.pythonanywhere.com/).

    **2. Set Up a New Web App**

   1. Log in to your PythonAnywhere account.

    2. Go to the "Dashboard" and click on the "Web" tab.

    3. Click on the "Add a new web app" button.

    4. Choose "Manual Configuration."

    5. Select the Python version you want to use (e.g., Python 3.8).

    6. Choose the option to configure the web app manually.

    7. Set the source code directory to your backend project directory.

    8. Set the working directory to your backend project directory.

    **3. Install Dependencies**

    In the PythonAnywhere console, install the required dependencies:

    ```bash
        pip install -r requirements.txt
    ```

    **4. Set Up Database**

   If you are using a database, migrate your database:

    ```bash
        python manage.py migrate
    ```

    **5. Configure Web App**

    1. Go back to the "Web" tab on PythonAnywhere.

    2. Find the section titled "Code" and update the "WSGI configuration file" to point to your `wsgi.py` file:

    ```bash
        import os
        import sys

        path = '/library'
        if path not in sys.path:
            sys.path.append(path)

        from django.core.wsgi import get_wsgi_application
        from django.contrib.staticfiles.handlers import StaticFilesHandler

        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "library.settings")

        application = StaticFilesHandler(get_wsgi_application())
    ```

    **6. Reload the Web App**

    Go back to the "Web" tab on PythonAnywhere, find the section titled "General," and click on the "Reload" button to apply the changes.

    **7. Access Your App**

    Your backend should now be hosted on PythonAnywhere. Access it through the provided PythonAnywhere subdomain (e.g., `yourusername.pythonanywhere.com`).


## Links

- Backend Repository: [Link to Backend Repo](https://github.com/kiranrokkam09/library)
- Frontend Repository: [Link to Frontend Repo](https://github.com/kiranrokkam09/library_static)
- Backend Deployment: [Link to Deployed Backend](https://kiran1432.pythonanywhere.com)
- Frontend Deployment: [Link to Deployed Frontend](https://library-static-1owi.vercel.app/)

## Documentation

Detailed design and implementation choices are documented in the `/docs` directory.

## NOTE:
Only Admin can create members in the library. The default credentials of Admin are **Username: "admin"** and **Password: "admin"**. 
