# HNGx REST API

---

A submission for task 2 of HNG's backend track.

---

This is a simple RESTful API made using Flask and sqlite3 as a database that allows you to perform CRUD (Create, Read, Update, Delete) operations on a 'Person' resource.

## Table of Contents

- [Getting Started](#getting-started)
	- [Prerequisites](#prerequisites)
	- [Installation](#installation)
- [Usage](#usage)
	- [Endpoint Overview](#endpoint-overview)
	- [Request Examples](#example-requests)
- [API Documentation](#api-documentation)

## Getting Started

### Prerequisites

Before starting, ensure you have the following installed:

- Python 3.x
- Flask
- Virtualenv
- (Optional) Requests for testing the API endpoints
- (Optional) A tool like Postman for testing the API endpoints

### Installation

On the terminal, run the following commands to:

1. Clone the repository:

```bash
git clone https://github.com/SidKay/HNGx-REST-API.git
```

2. Navigate to the project directory:

```bash
cd HNGx-REST-API
```

3. Install `virtualenv` for Python:

```bash
pip install virtualenv
```

4. Create a virtual environment and activate it:

```bash
python -m venv <env_name> && <env_name>\Scripts\activate
```

5. Install the required python packages:

```bash
pip install -r requirements.txt
```

6. Run the application:

```bash
python api.py
```

This will run the app locally at `http://localhost:5000`.

## Usage

### Endpoint Overview

- `POST/api`: Creates a new person.
- `GET/api/<id>`: Retrieves the details of a person using ID.
- `PUT/api/<id>`: Updates the details of a person using ID.
- `DELETE/api/<id>`: Deletes a person's details.

### Request Examples

1. **Create a person:**

```http
POST http://localhost:5000/api
Content-Type: application/json

{
	'name': 'Flint Lockwood',
	'track': 'Backend',
	'age': 30
}
```

2. **Retrieve a person using ID:**

```http
GET http://localhost:5000/api/1
```

3. **Update an existing person using ID:**

```http
PUT http://localhost:5000/api/1
Content-Type: application/json

{
	'name': 'Baelin',
	'track': 'Product Design',
	'age': 32

}
```

4. **Delete an existing person using ID:**

```http
DELETE http://localhost:5000/api/1
```

## API Documentation

For detailed API documentation, please refer to the [API Documentation](DOCUMENTATION.md) file.
