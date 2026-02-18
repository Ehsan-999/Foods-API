# Foods API

## Description
Foods API is a simple RESTful API built with **FastAPI** to manage food items.  
It supports full **CRUD operations** (Create, Read, Update, Delete) and allows exporting all food data as a **JSON file**.  
This project demonstrates **basic data persistence** using a local JSON file and proper input validation with **Pydantic**.

---

## Features

- ✅ List all foods
- ✅ Get a single food item by ID
- ✅ Create a new food
- ✅ Update an existing food
- ✅ Delete a food item
- ✅ Export all foods as JSON file
- ✅ Input validation with Pydantic

---

## Tech Stack

- **Python 3.11+**
- **FastAPI** – Web framework for APIs
- **Pydantic** – Data validation
- **UUID** – Unique IDs for food items
- **JSON** – Simple persistent storage

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/ehsan-999/fastapi-foods.git
cd fastapi-foods
```


### 2. Install dependencies

```bash
pip install fastapi uvicorn pydantic
```


### 3. Run the server
```bash
uvicorn main:app --reload
```
The API will be available at:

```bash
http://127.0.0.1:8000
```
---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | /foods           | List all foods |
| GET    | /foods?export=1  | Export all foods as JSON |
| GET    | /foods/{food_id} | Get a single food by ID |
| POST   | /foods           | Create a new food |
| PUT    | /foods/{food_id} | Update an existing food |
| DELETE | /foods/{food_id} | Delete a food item |

---

## Example Requests

### Create a New Food

```http
POST /foods
Content-Type: application/json

{
  "title": "Banana",
  "category": "Fruit",
  "description": "Yellow fruit",
  "estimated_time": 3,
  "difficulty": "easy"
}
```

### Response
```json
{
  "id": "e1b2c3d4-5678-9101-2345-abcdef123456",
  "title": "Banana",
  "category": "Fruit",
  "description": "Yellow fruit",
  "estimated_time": 3,
  "difficulty": "easy"
}
```
--- 

### Export Foods as JSON

```bash
GET /foods?export=1
```

- The JSON file will be saved in:
```bash
data/foods.json
```

- The file will also be returned as a downloadable response.

---

### Data Persistence

- The API loads data from data/foods.json on startup (if the file exists).

- Food data is stored locally using JSON.

- This provides simple persistence without using a database.

--- 

### Running with Auto Docs (Swagger UI)
FastAPI automatically provides interactive API documentation:

- Swagger UI:
```bash
http://127.0.0.1:8000/docs
```

- ReDoc:
```bash
http://127.0.0.1:8000/redoc
```

--- 
### Project Structure
```css
.
├── main.py
├── data/
│   └── foods.json
└── README.md
```
