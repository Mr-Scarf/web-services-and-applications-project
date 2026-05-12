
# Web Services and Applications

**University**: Atlantic Technological University  
**Module**: Web Services and Applications   
**Class**: January 2026  
**Author**: David Scally  


# Project - Guinness Pint App

## Purpose

The project is to create a web application using Flask & RESTful APIs to perform CRUD (Create, Read, Update, Delete) operations on 
data stored in a SQLite database. 


This application allows users to view, add, update & delete Guinness prices for pubs.

## Live Application

Hosted on PythonAnywhere:

[Guinness Pint App](https://mrscarf.eu.pythonanywhere.com/)

## Features

 - View all pint prices
 - Add a new pub & pint price
 - Update existing pint price
 - Delete pub pint entry

## API Endpoints

- GET/pints - List all pint prices
- GET/pints/<id> - List specific pint price by pub ID
- POST/pints - Create a new pint entry
- PUT/pints/<id> - Update an existing pint entry by pub ID
- DELETE/pints/<id> - Delete a specific pint entry

## Project Structure

```text
├── staticpages/  
│       ├── index.html      # Frontend webpage using AJAX & Javascript  
│       ├── styles.css      # CSS styling layout of frontend webpage  


├── pint_app.py             # Flask application routes  
├── pint_dao.py             # Data access object for SQLite database  
├── pints.db                # SQLite database file  
├── requirements.txt        # Project dependencies  
├── createschema.py         # Script to create SQLite database table  
└── README.md               # This file, project documentation & installation.  
```

## Technologies Used

 - Python
 - Flask
 - SQLite
 - CSS
 - HTML
 - JavaScript
 - AJAX
 - PythonAnywhere


## Installation & Setup

1. **Clone the repository**

```bash
git clone https://github.com/Mr-Scarf/web-services-and-applications-project.git
cd web-services-and-applications-project
```

2. **Create a virtual environment**
```bash
python -m venv venv 
venv\Scripts\activate
```

3. **Install dependencies - see file 'requirements.txt'**

```bash
pip install -r requirements.txt
```

4. **Create the database**
```bash
python createschema.py
```

5. **Run the application**
```bash
python pint_app.py
```

6. **Open in browser:**

http://127.0.0.1:5000/


  


