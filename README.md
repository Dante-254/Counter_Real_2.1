# Django Search App

A Django application that provides an intuitive search interface for finding properties based on various filters. Users can search for properties, with options to filter by bedrooms, bathrooms, and price range.

## Features

- Filter by:
  - Number of bedrooms
  - Number of bathrooms
  - Price range
- User-friendly interface
- Responsive design

## Technologies Used

- Django
- PostgreSQL
- Bootstrap (for frontend design)
- HTML/CSS/JavaScript

## Installation

### Prerequisites

- Python 3.x
- Django
- PostgreSQL
- Git

### Steps to Install

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/django-search-app.git
   cd django-search-app
2. Create a virtual environment:

	`python -m venv venv`
  `source venv/bin/activate`  # On Windows use `venv\Scripts\activate`

3. Install the required packages:

	`pip install -r requirements.txt`

4. Set up the PostgreSQL database:

   Create a new database in PostgreSQL.
   Update the DATABASES setting in `settings.py` with your database credentials.
5. Apply migrations:
   
 	`python manage.py migrate`
 
6. Run the development server:
    
 	`python manage.py runserver`

 
Visit `http://127.0.0.1:8000/` in your web browser to see the app in action.

