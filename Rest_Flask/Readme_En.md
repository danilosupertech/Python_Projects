# User Management API with Flask and SQLite

## 🚀 Project Description
This project is a simple **User Management API** built with **Flask** and **SQLite**.  
It allows you to **create, list, update and delete users** through HTTP requests.

---

## 📦 Requirements
Before starting, make sure you have installed:

- [Python 3.8+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/)
- [Flask](https://flask.palletsprojects.com/)
- [SQLite](https://www.sqlite.org/index.html)
- [Postman](https://www.postman.com/) (optional, for testing)

---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/flask-sqlite-api.git
cd flask-sqlite-api
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate    # Windows
```

### 3. Install dependencies
```bash
pip install flask
```

### 4. Run the application
```bash
python app.py
```
The server will run on: `http://localhost:5500`

---

## 📌 Endpoints

### ➤ Create a user (POST)
`http://localhost:5500/users`

**Request Body (JSON):**
```json
{
  "id": 1,
  "name": "Danilo",
  "email": "danilo@tech.com"
}
```

---

### ➤ List all users (GET)
`http://localhost:5500/users`

---

### ➤ Get a specific user by ID (GET)
`http://localhost:5500/users/1`

---

### ➤ Update a user (PUT)
`http://localhost:5500/users/1`

**Request Body (JSON):**
```json
{
  "name": "Danilo Updated",
  "email": "danilo@newmail.com"
}
```

---

### ➤ Delete a user (DELETE)
`http://localhost:5500/users/1`

---

## 🛠 Testing with Postman

You can import the collection into **Postman** and test the endpoints easily.

Example request in Postman:
```
POST http://localhost:5500/users?id=2&name="Danilo"&email="danilo@tech.com"
```

---

## 📂 Project Structure
```
flask-sqlite-api/
│── app.py         # Main application
│── users.db       # SQLite database
│── README.md      # Documentation
```

---

## ✅ Next Steps
- Add authentication (JWT)
- Add pagination for users
- Deploy to a cloud service (Render, Railway, Heroku)
