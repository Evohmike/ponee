# ponee
> A lightweight Django template ready for Heroku

## Motivation

Loosely inspired by the beloved django-cookiecutter, ponnee is a lightweight Django template without too many assumptions.

## What's included

- Custom user
- 12-Factor based setting via [django-environ](https://github.com/joke2k/django-environ)
- Requirements for production and development
- Django REST framework
- Django CORS headers
- Security settings
- Heroku support with [django-heroku](https://github.com/heroku/django-heroku)
- Testing and coverage

Ponee uses sqlite3 for development but you can easily switch to PostgreSQL by tweaking `settings.base.py`.

## Installation

Prepare a virtual environment in a folder of choice and install Django:

```bash
mkdir mynewproject && cd $_
python3 -m venv venv
source venv/bin/activate
pip install django
```

Then install the template:

```bash
django-admin startproject \ 
    --template https://github.com/valentinogagliardi/ponee/archive/master.zip \
    --name=Procfile \
    --extension=py,example yournewproject .
```

Install the dependencies:

```bash
pip install -r ./requirements/dev.txt
```

Copy the example env to `.env` and adjust the variables as you wish:

```bash
mv .env.example .env
```

Before starting off make the migrations for the custom User:

```bash
python manage.py makemigrations
python manage.py migrate
```

and your good to runserver!

## Environment variables

See `.env.example` for a complete list

## Deploy on Heroku

Before starting off you should have a Git repo in your project folder:

```bash
git init
```

Login on Heroku with the Heroku toolbelt:

```bash
heroku login
```

Create a new app (you can change the name later):

```bash
heroku apps:create --region eu
```

Copy the example `.env.prod.example` to `.env.prod` and run:

```bash
python configure_prod_envs.py
```

The script reads all the env variables from `.env.prod` and runs `heroku config:set` for each one.

Finally make a commit and push the code:

```bash
git add .
git commit -m "First commit"
git push heroku master
```

## Test

Running tests:

```bash
python manage.py test
```

Running tests with coverage:

```bash
coverage run --omit='*/venv/*' manage.py test
coverage report
```
