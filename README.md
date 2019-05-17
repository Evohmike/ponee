# ponee
> A lightweight Django template

## Motivation

Loosely inspired by django-cookiecutter, ponnee is a lightweight Django template without too many assumptions.

## What's included

- Custom user
- 12-Factor based setting via [django-environ](https://github.com/joke2k/django-environ)
- Requirements for production and development
- Django REST framework
- Django CORS headers
- Security settings
- Heroku support with [django-heroku](https://github.com/heroku/django-heroku)
- Testing and coverage

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
    --template https://github.com/valentinogagliardi/ponee/archive/master.zip
    --name=Procfile
    --extension=py .
```

## Environment variables

See `.env.example` for a complete list

## Deploy on Heroku

TODO

## Test

```bash
pip install -r ./requirements/dev.txt
```

TODO