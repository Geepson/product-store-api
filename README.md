# 🛒 Product Store REST API

A RESTful API for managing products and categories using Django REST Framework (DRF). This project allows users to perform full CRUD operations on products and categories. It is designed with clean JSON responses and tested using Postman.

---

## 🚀 Features

- ✅ Full CRUD for products and categories
- ✅ Django REST Framework (DRF) powered API endpoints
- ✅ SQLite database for quick development
- ✅ Clean, structured JSON responses
- ✅ Modular design ready for scaling
- 🧪 Tested using Postman

---

## 🛠 Tech Stack

- **Backend**: Django, Django REST Framework (DRF)
- **Language**: Python
- **Database**: SQLite (development)
- **Tools**: Postman, Git

---

## 📁 Project Structure

product_api/
├── product_api/ # Django project settings
├── store/ # Main app with models, views, serializers, URLs
│ ├── models.py
│ ├── views.py
│ ├── serializers.py
│ ├── urls.py
├── manage.py
├── requirements.txt
└── README.md


## 🧑‍💻 API Endpoints

Base URL: `/api/`

| Endpoint               | Method | Description                  |
|------------------------|--------|------------------------------|
| `/products/`           | GET    | List all products            |
| `/products/`           | POST   | Create a new product         |
| `/products/<id>/`      | GET    | Retrieve a single product    |
| `/products/<id>/`      | PUT    | Update full product details  |
| `/products/<id>/`      | PATCH  | Partially update a product   |
| `/products/<id>/`      | DELETE | Delete a product             |
| `/categories/`         | GET/POST | List or create categories   |

---

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/product-store-api.git
cd product-store-api
2. Create and Activate a Virtual Environment
bash
Copy
Edit
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Run Migrations
bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
5. Start Development Server
bash
Copy
Edit
python manage.py runserver
Now open your browser and go to:

bash
Copy
Edit
http://localhost:8000/api/
🔑 Example JSON for POST /products/
{
  "name": "Gaming Mouse",
  "description": "High precision RGB gaming mouse",
  "price": 49.99,
  "stock": 100,
  "category": 1
}
✅ Make sure the category ID already exists.

🧪 Testing with Postman
Import endpoint: http://localhost:8000/api/products/

Use POST, PUT, PATCH, DELETE as needed

Set headers:

Content-Type: application/json

If auth enabled: Authorization: Token <your_token>

🔒 Authentication (Optional)
To enable token authentication:

Add rest_framework.authtoken to INSTALLED_APPS

Run:

python manage.py migrate
Create token for user:

from rest_framework.authtoken.models import Token
Token.objects.create(user=<your_user>)
📜 License
This project is open-source and free to use under the MIT License.

🙋‍♂️ Author
Gipson Giri
Aspiring Python/Django Developer

