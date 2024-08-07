# Reflex Tutorial Blog Site

This is a Python-based blog site built using the Reflex framework. It showcases various functionalities including user authentication, blog management, article details, and contact forms.

## Installation

To get started with this project, follow these steps:

1. **Clone the Repository**

   ``` git clone <repository-url> ```

   ``` cd <repository-directory>```

2. **Create a Virtual Environment**

    ``` python -m venv venv ```
    ``` source venv/bin/activate ```

    On Windows use `venv\Scripts\activate`

3. **Install Dependencies**

    ``` pip install -r requirements.txt ```


1. **Configure Reflex**
    Edit rxconfig.py with your configuration details.

1. **Usage**

    ```reflex db init``` # initalize sqlite db


    ``` reflex db makemigration ``` # create database schemas

    ``` reflex db migrate ``` # create db

    ``` reflex run ``` # start application

**More Info**
checkout ``https://reflex.dev/`` for more information on reflexs
