# HNGx REST API Documentation

## Introduction

This is the documentation for the HNGx REST API. This API provides various endpoints to perform CRUD (Create, Read, Update, Delete) operations on a 'Person' resource.

Here, you can understand how to interact with the API, its endpoint details, request and response formats, and a few sample use cases.

## Table of Contents

- [API Basics](#api-basics)
	- [Base URL](#base-url)
- [Endpoints](#endpoints)
  	- [Create a Person](#create-a-person)
  	- [Retrieve a Person](#retrieve-a-person)
  	- [Update a Person](#update-a-person)
  	- [Delete a Person](#delete-a-person)
- [Request and Response Formats](#request-and-response-formats)
- [Examples](#examples)
- [Error Handling](#error-handling)

## API Basics

### Base URL

The base URL for the API endpoints is:

```
https://sidney.pythonanywhere.com/api
```

## Endpoints

### Create a Person

- **Endpoint:** `/api`
- **HTTP Method:** POST
- **Description:** Create a new person.
- **Request:** A JSON object representing the person to be created.
- **Response:** A JSON object showing that a person has been created.

### Retrieve a person

- **Endpoint:** `/api/{id}`
- **HTTP Method:** GET
- **Description:** Retrieve the details of a person using ID.
- **Response:** A JSON object representing the person.

### Update a person

- **Endpoint:** `/api/{id}`
- **HTTP Method:** PUT
- **Description:** Update an existing person using ID.
- **Request:** A JSON object representing the updated person.
- **Response:** A JSON object showing that a person has been updated.

### Delete a person

- **Endpoint:** `/api/{id}`
- **HTTP Method:** DELETE
- **Descriprion:** Delete a person using ID.
- **Response:** A JSON object showing that a person has been deleted.

## Request and Response Formats

### Person Object

- **Properties**
	- `id` (integer): The person's unique identifier.
	- `name` (string): Name of the person.
	- `track` (string): Development track of the person.
	- `age` (integer): Age of the person.

### Example Person Object

```json
{
	"id": 1,
	"name": "Lewis Hamilton",
	"track": "Product Design",
	"age": 21
}
```

## Examples

### Get a Person

**Request**

```http
GET http://https://sidney.pythonanywhere.com/api/1
```

**Response**

```json
{
	"id": 1,
	"name": "Lewis Hamilton",
	"track": "Product Design",
	"age": 21
}
```

### Create a Person

**Request**

```http
POST https://sidney.pythonanywhere.com/api
Content-Type: application/json

{
	"name": "Sylvester Stallone",
	"track": "Backend",
	"age": 36
}
```

**Response**

```json
{
	"message": "Person {name} added successfully."
}
```

### Update a Person

**Request**

```http
PUT https://sidney.pythonanywhere.com/api/4
Content-Type: application/json

{
  "name": "Person New Name",
  "track": "UI/UX",
  "age": 32
}
```

**Response**

```json
{
	"message": "Person has been updated successfully."
}
```

### Delete a Person

**Request**

```http
DELETE https://sidney.pythonanywhere.com/api/2
```

**Response:**

```json
{
	"message": "Person deleted successfully."
}
```

## Error Handling

The API provides appropriate HTTP status codes and error messages in the case of errors. Some of the errors are:

- **400 Bad Request:** If the request is missing fields when creating or updating a person.
- **404 Not Found:** It the person with the specified ID does not exist when retrieving, deleting or updating.
- **500 Internal Server Error:** If an unexpected error occurs within the server when processing a request.

---

For more information, feel free to contact the [API provider](https://github.com/SidKay).
