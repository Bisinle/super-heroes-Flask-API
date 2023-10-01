# Hero-Flask-Api

![python version](https://img.shields.io/badge/python-3.10.12-blue.svg)
![Flask version](https://img.shields.io/badge/flask-2.3.3-red.svg)
![Flask-RESTX version](https://img.shields.io/badge/Flask_RESTX-1.1.0-cyan.svg)
![Pytest version](https://img.shields.io/badge/pytest-7.4.2-white.svg)
[![license](https://img.shields.io/badge/license-%20MIT%20-green.svg)](./LICENSE)
![Gunicorn version](https://img.shields.io/badge/gunicorn-21.2.0-orange.svg)

<img src='./server/images/api.png'>

## Features

- Create a hero
- Get all heroes
- Find, update, or delete a hero by ID
- Create a power
- Get all powers
- Find, update, or delete a power by ID
- Associate hero with a power by creating HeroPower
- Find which hero has which power
- Find, update, or delete a HeroPower by ID
- Create a new HeroPower that is associated with an existing Power and Hero

## Installation

### 1. Clone the repository

```txt
git clone https://github.com/Bisinle/super-heroes-Flask-API
```

### 2. Navigate to the project's directory

```cd super-heroes-Flask-API

```

### 3. Install required dependencies

```pip install -r requirements.txt

```

### 4. Activate the virtual environment

```source venv/bin/activate

```

### 5. If needed, seed the database with

```python
python3 seed.py
```

### 6. Run the Flask server from the root directory

```python
python3 run.py
```

### 7. Use an API management tool e.g., `Postman` / `Insomnia` to make requests

## Usage
