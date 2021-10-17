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
### Staging

https://gamily-heroku.herokuapp.com/

### Production

https://gamily-api.herokuapp.com/ 

### Deploying to Heroku

set up git remote config:
```
heroku	https://git.heroku.com/gamily-heroku.git (fetch)
heroku	https://git.heroku.com/gamily-heroku.git (push)
heroku-staging	https://git.heroku.com/gamily-heroku.git (fetch)
heroku-staging	https://git.heroku.com/gamily-heroku.git (push)
```
Execute the following:
```
git push <remote-ref> main # heroku/heroku-staging or whatever you customized
heroku run python3 manage.py migrate # optional if your changes have an impact on data model
```


### Special notes

Auth endpoints listed here:
https://dj-rest-auth.readthedocs.io/en/latest/api_endpoints.html
