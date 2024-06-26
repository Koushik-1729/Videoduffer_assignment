# Flask API on AWS EC2

This project implements a Flask API hosted on an AWS EC2 instance. The API accepts JSON POST requests containing user data, stores the data in an SQLite database, and returns a JSON response containing names with IDs above 5.

## Introduction

This Flask API provides a simple interface for storing user data and retrieving names with IDs above 5. It utilizes Flask for web server functionality and SQLite for database management.

## Features

- Accepts JSON POST requests with user data.
- Stores user data in an SQLite database.
- Returns JSON response containing names with IDs above 5.

## Technologies Used

- Python: The primary programming language used for the backend logic.
- Flask: A lightweight web framework used for creating the API endpoints.
- SQLite: A lightweight relational database used for storing user data.
- AWS EC2: A cloud computing service used to host the Flask application.

## Setup

1. **Install Dependencies**: Ensure that Python, Flask, and SQLite are installed on your local machine.
   
2. **Clone the Repository**: Clone this repository to your local machine using the following command:
   

3. **Navigate to the Project Directory**: Open a terminal and navigate to the project directory:


4. **Install Dependencies**: Install the required Python dependencies using pip:


5. **Create SQLite Database**: Create an empty SQLite database file named `database.db` in the project directory:


## Usage

1. **Run the Flask Application**: Start the Flask application by running the following command:


2. **Send Requests to the API**: Use an HTTP client like Postman to send JSON POST requests to the API endpoint:


The input should be in the following format:

```json
{
    "name": "xyz",
    "id": 100
}
```
response:
```json

{
    "names_with_ids_above_5": ["xyz", "abc"]
}
```

## Testing
1. **Test with Postman**:Use Postman or any other HTTP client to send JSON POST requests to the API endpoint.
2. **Verify Response**: Verify that the API returns the expected JSON response.

## Deployment
1. **Launch an EC2 Instance**: Launch an EC2 instance on AWS with an appropriate configuration, such as an Ubuntu server.
2. **Connect to EC2 Instance**: Connect to the EC2 instance using SSH and the generated .pem key:
Copy code
```bash

ssh -i "D:\inlustro backend\Videodubber.pem" ec2-user@your-ec2-public-ip
``` 
3. **Install Dependencies**: Install necessary dependencies on the EC2 instance.
4. **Start the App**: export FLASK_APP=App.py
5. **command to  run in backround** nohup flask run --host=0.0.0.0
6. **Run Flask Application**: Run the Flask application using a web server like Gunicorn or uWSGI.