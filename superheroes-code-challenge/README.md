# 🦸 Flask Superheroes API

A RESTful Flask API for managing a collection of superheroes, their powers, and their associated hero powers. Built with SQLAlchemy ORM, this project demonstrates model relationships, validations, and full CRUD functionality.

---

## 📁 Project Structure

```
.
├── venv/
├── server/
│ ├── app.py
│ ├── models.py
│ ├── seed.py
│ ├── config.py
│ └── migrations/
├── Pipfile
├── Pipfile.lock
└── README.md

```


---

## 🚀 Features

- View all superheroes and their powers
- View all powers with descriptions
- Assign powers to heroes with strength levels
- Update power descriptions
- Cascading deletes with relationships
- Data validations on power descriptions and strength levels

---
## 🗃️ Models

- **Hero**
  - `id`: Integer, primary key
  - `name`: String
  - `super_name`: String

- **Power**
  - `id`: Integer, primary key
  - `name`: String
  - `description`: String _(at least 20 characters)_

- **HeroPower**
  - `id`: Integer, primary key
  - `strength`: String _(choices: Strong, Weak, Average)_
  - `hero_id`: ForeignKey → Hero
  - `power_id`: ForeignKey → Power

---

## 🔁 Relationships

- A `Hero` has many `Powers` through `HeroPowers`
- A `Power` has many `Heroes` through `HeroPowers`
- A `HeroPower` belongs to both a `Hero` and a `Power`
- Deleting a hero or power cascades to delete related `HeroPowers`

---

## 🧪 Validations

- **Power**: `description` must be at least 20 characters
- **HeroPower**: `strength` must be `'Strong'`, `'Weak'`, or `'Average'`

---
## 🔗 API Endpoints

### Heroes
| METHOD | ROUTE             | DESCRIPTION                              |
|--------|------------------|------------------------------------------|
| GET    | `/heroes`        | Returns all heroes (without powers)      |
| GET    | `/heroes/<id>`   | Returns hero by ID with nested powers    |

### Powers
| METHOD | ROUTE             | DESCRIPTION                              |
|--------|------------------|------------------------------------------|
| GET    | `/powers`        | Returns all powers                       |
| GET    | `/powers/<id>`   | Returns a single power                   |
| PATCH  | `/powers/<id>`   | Updates power description                |

### Hero Powers
| METHOD | ROUTE             | DESCRIPTION                              |
|--------|------------------|------------------------------------------|
| POST   | `/hero_powers`   | Assigns a power to a hero                |

---

## ⚙️ Setup Instructions

### 1. Clone the repo:
   ```bash 
   git clone https://github.com/Larr-y1/Phase-4-Code-Challenge-Superheroes-.git
   cd Phase-4-Code-Challenge-Superheroes
   ```

### 2.Create and activate virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate    # macOS/Linux
venv\Scripts\activate    # Windows
```

### 3.Install dependencies using Pipenv (recommended):
```bash
pip install pipenv
pipenv install
```

### 4.Set environment variables
```bash
export FLASK_APP=app.py
export FLASK_ENV=development
```

### 5.Run migratios and seed the database
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
python seed.py
```

### 6.Start the server
```bash
flask run
```
---

## 📄 License
This project is open source and available under the MIT License.
