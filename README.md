# Onboaiding sample application

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/Artlikeme/onboarding.git
$ cd onboarding_system
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python -m venv env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```

Once `pip` has finished downloading the dependencies:
```sh
(env)$ python manage.py migrate
```
```sh
(env)$ python manage.py runserver
```
```sh
(env)$ python manage.py createsuperuser
```
And navigate to `http://127.0.0.1:8000/admin` for creation Surveys and questions.\
Navigate to `http://127.0.0.1:8000/` to see list of surveys.
