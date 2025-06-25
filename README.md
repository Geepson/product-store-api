# Product Store API

A RESTful API for managing products and categories using Django REST Framework.

## Features
- CRUD for products and categories
- Token-based authentication (optional)
- JSON responses
- Tested with Postman

## Setup
```bash
git clone https://github.com/Geepson/product-store-api.git
cd product-store-api
python -m venv venv
source venv/bin/activate(MAC)
venv\Scripts\activate(Windows)

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
