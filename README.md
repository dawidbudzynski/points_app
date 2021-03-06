# Simple Point App

## https://simple-points-app.herokuapp.com/

## General info

A web application made using Python 3, Django 2, and PostgreSQL.  
<br/>Application allows import users from csv file and change their balance.

## Main functions

* importing users from csv file using management command
* displaying all users 
* making changes to users balance

## Technologies

* Python 3.7
* Django 2.2
* PostgreSQL

## Setup

To run this project locally:

1. In docker-compose.yaml replace `temporary_secret_key` with your own secret
   key (https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/#secret-key)
2. Start containers with

```
docker-compose up
```

3. Application will be available at `http://0.0.0.0:8000/`

## Heroku deployment

To deploy application to Heroku:

1. Sign up to Heroku account and install Heroku CLI https://devcenter.heroku.com/articles/heroku-cli
2. In Heroku dashboard create new application
3. In CLI connect to remote of your application

```
heroku git:remote -a <your-application-name>
```

4. Log in to Container Registry

```
heroku container:login
```

5. Build a local image with correct tag

```
docker build -t registry.heroku.com/<your-application-name>/web .
```

6. Push your secret key

```
heroku config:set SECRET_KEY=SOME_SECRET_VALUE -a <your-application-name>
```

7. Create and connect PostgreSQL

```
heroku addons:create heroku-postgresql:hobby-dev -a <your-application-name>
```

8. Push local image to Heroku registry

```
docker push registry.heroku.com/<your-application-name>/web
```

9. Release changes

```
heroku container:release -a <your-application-name> web
```

10. Run `manage.py migrate` on Heroku

```
heroku run python manage.py migrate
```