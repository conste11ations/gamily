# gamily

### Setup for local development

```
git clone git@github.com:conste11ations/gamily.git
cd gamily
pip install virtualenv
virtualenv venv
source venv/bin/activate
pip3 install django
python3 -m django --version // check
pip3 install djangorestframework
// install postgresql
// create user admin with password
// create database gamily with owner admin
pip3 install psycopg2-binary
pip3 install python-dotenv 
// create .env file in root dir
python3 manage.py migrate
python3 manage.py runserver // default port at 8000
```
### Special notes

Auth endpoints listed here:
https://dj-rest-auth.readthedocs.io/en/latest/api_endpoints.html
