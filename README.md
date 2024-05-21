# Project Description

* FastAPIs of following route groups are created: 


       /users/me
       /users/all
        
       And,
        
       /items/all
       /items/{item_id}

* Implemented an OAuth2 based authentication system 
      
* To test APIs, we use Pytest framework.

## Prerequisites

* Python3
* FastApi
* Pytest
* OAuth2
* Git
* Virtualenv

## How to setup
1. Create a virtual environment to install dependencies in and activate it. This is needed to make sure the system uses python3 for further execution.
- Create a virtual env using python3: `python3 -m venv env`
- Activate the virtualenv: `source env/bin/activate`
 

2. Clone the source code through GitHub CLI:  
`gh repo clone geeky-nomad/PowerBI` and checkout to `development` branch

3. Upgrade pip version:
`python3 -m pip install --upgrade pip`

4. Install all the dependencies inside virtualenv:
`pip3 install -r requirements.txt` 

## How to execute
1. Start FastApi app's server:
 `uvicorn main:app --reload`

2. Navigate to use the API Swagger documentation:
`http://127.0.0.1:8000/docs`


## How to execute TestCases

Command: `$ pytest --disable-pytest-warnings`

## Good to know information:
1. All the static data can be found inside `models/` directory
