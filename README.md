# Library Management System - Backend

This repository contains the backend implementation of a Library Management System, providing REST APIs for managing books, members, and user authentication.

## Table of Contents
1. [Scenario](#scenario)
2. [Backend Structure](#backend-structure)
3. [Database Structure](#database-structure)
4. [API Documentation](#api-documentation)


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

