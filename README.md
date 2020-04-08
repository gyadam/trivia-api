# Trivia API

### Overview

Trivia API is a backend web development project created for the Full Stack Developer Nanodegree at Udacity. The goal of the project was to:

* Create all necessary endpoints on the backend to serve the frontend, enabling the visitor of the website to:
    * View all trivia questions stored in a database
    * View trivia questions based on their category
    * Add and delete questions to the database
    * Play trivia in a chosen category, getting random questions from the database
* Apply test-driven development, writing unit tests for each endpoint
* Make modifications to the frontend and database if necessary

The site runs on localhost and was created only for educational purposes.

### Tech stack

* **SQLAlchemy ORM** as the ORM library
* **PostgreSQL** for the database
* **Python3** and **Flask** as the server language and server framework
* **HTML**, **CSS**, and **Javascript** with **Node.js** for the frontend

### Endpoints

All endpoints accept JSON encoded requests and return JSON encoded bodies. The following endpoints were implemented to serve requests from the frontend, interacting with the database:

```/questions```
* GET request:
    * 
* POST request:
    *

```/questions/\<int:question_id\>```
* DELETE request:

```/categories```
* GET request

```/categories/\<int:category_id\>/questions```
* GET request:

```/add```
* GET request:

```/quizzes```
* POST request:


### Development setup

**Virtual environment**

To start and run the local development server, initialize and activate a virtual environment:

```
$ cd YOUR_PROJECT_DIRECTORY_PATH/
$ virtualenv --no-site-packages env
$ source env/bin/activate
```

Install dependencies:
```
$ pip install -r requirements.txt
```

Key Dependencies:

* **Flask** is a lightweight backend microservices framework. Flask is required to handle requests and responses.
* **SQLAlchemy** is the Python SQL toolkit and ORM that handles the lightweight sqlite database.
* **Flask-CORS** is the extension used to handle cross origin requests from the frontend server.

**Database Setup**

With Postgres running, restore a database using the trivia.psql file provided. After creating a database called ```trivia```, from the backend folder in terminal run:

``` psql trivia < trivia.psql ```

**Running the server**

To run the server, execute:

```
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

**Running the frontend**

First, install [Node.js and npm](https://nodejs.org/en/).

Then, to run the frontend, execute:
```
npm start
```
