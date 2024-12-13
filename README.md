# Car and Part Management API 🚗🔧

This is a simple **FastAPI** project for managing cars and their parts. It provides basic CRUD functionality for cars and parts, making it a great starting point for learning FastAPI.

---

## Features ✨

- 🚗 List all cars.
- ➕ Add a new car.
- 🔧 List all parts.
- 🔍 Retrieve a part by ID.
- ➕ Add a new part.
- ✏️ Update an existing part.
- ❌ Delete a part.

---

## Endpoints 🌐

### 1. **List All Cars** 🚗
**GET** `/carros`

Retrieve the list of all cars.

**Response:**
```json
{
  "status": "success",
  "message": "Carros recuperados com sucesso.",
  "data": [...]
}
```

---

### 2. **Add a New Car** ➕
**POST** `/carros`

**Form Data:**
- `nome` (string, required)
- `modelo` (string, required)

**Response:**
```json
{
  "status": "success",
  "message": "Carro adicionado com sucesso.",
  "data": {...}
}
```

---

### 3. **List All Parts** 🔧
**GET** `/pecas`

Retrieve the list of all parts.

**Response:**
```json
{
  "status": "success",
  "message": "Peças recuperadas com sucesso.",
  "data": [...]
}
```

---

### 4. **Retrieve Part by ID** 🔍
**GET** `/pecas/{peca_id}`

Retrieve the details of a part using its unique ID.

**Response (if found):**
```json
{
  "status": "success",
  "message": "Peça recuperada com sucesso.",
  "data": {...}
}
```

**Response (if not found):**
```json
{
  "detail": "Peça não encontrada."
}
```

---

### 5. **Add a New Part** ➕
**POST** `/pecas`

**Form Data:**
- `nome` (string, required)
- `descricao` (string, required)
- `preco` (float, required)
- `carro_id` (int, required)

**Response:**
```json
{
  "status": "success",
  "message": "Peça adicionada com sucesso.",
  "data": {...}
}
```

**Response (if car not found):**
```json
{
  "detail": "Carro associado não encontrado."
}
```

---

### 6. **Update a Part** ✏️
**PUT** `/pecas/{peca_id}`

Update an existing part's details using its ID.

**Form Data:**
- `nome` (string, required)
- `descricao` (string, required)
- `preco` (float, required)
- `carro_id` (int, required)

**Response:**
```json
{
  "status": "success",
  "message": "Peça atualizada com sucesso.",
  "data": {...}
}
```

**Response (if part or car not found):**
```json
{
  "detail": "Peça não encontrada."
}
```
```json
{
  "detail": "Carro associado não encontrado."
}
```

---

### 7. **Delete a Part** ❌
**DELETE** `/pecas/{peca_id}`

Delete a part by its ID.

**Response:**
```json
{
  "status": "success",
  "message": "Peça removida com sucesso.",
  "data": {...}
}
```

**Response (if not found):**
```json
{
  "detail": "Peça não encontrada."
}
```

---

## How to Run 🚀

### Prerequisites

- 🐍 Python 3.9 or higher installed.
- 🛠 Install dependencies.

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repository-url.git
   cd your-repository
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Start the development server:
   ```bash
   uvicorn main:app --reload
   ```

4. Open your browser and navigate to:
   - API Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) 📄
   - Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) 📚

---

## License 📜

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
