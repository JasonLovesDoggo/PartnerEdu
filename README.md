# PartnerEDU

A CMS for schools

## Basic Commands

### Setting Up Your Users

- To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

- To create a **superuser account**, use this command:

      $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ mypy partneredu

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest
### Sentry

Sentry is an error logging aggregator service. You can sign up for a free account at <https://sentry.io/signup> or download and host it yourself.
The system is set up with reasonable defaults, including 404 logging and integration with the WSGI application.

You must set the DSN url in production.

## Translations
PartnerEDU is a multilingual project. It uses Django's internationalization system to provide a translation of the site's content. The project is set up to support multiple languages, and the user can switch between them.
for more information, please check the [Django documentation](https://docs.djangoproject.com/en/stable/topics/i18n/translation/) and our documentation [here](https://github.com/JasonLovesDoggo/fbla/blob/fdde017e1fe81d0ce4d4d432d494d75dce893644/locale/README.md).

## Setup

1. Clone the repo
2. Create a virtual environment with `python3 -m virtualenv venv`
3. Activate the virtual environment with `source venv/bin/activate` on Linux or `.\venv\Scripts\activate` on Windows
4. Install the requirements with `pip install -r requirements/local.txt`
5. Run the migrations with `python manage.py migrate`
6. Create a superuser with `python manage.py createsuperuser`
7. Run the server with `python manage.py runserver`

## Deployment

The following details how to deploy this application.

### Docker

See detailed [Django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).

##### Common Commands

> You will need to build the stack first. To do that, run:

`docker compose -f production.yml build`

> Once this is ready, you can run it with:

`docker compose -f production.yml up`
> To run the stack and detach the containers, run:

`docker compose -f production.yml up -d`
> To run a migration, open up a second terminal and run:

`docker compose -f production.yml run --rm django python manage.py migrate`
> To create a superuser, run:

`docker compose -f production.yml run --rm django python manage.py createsuperuser`
> If you need a shell, run:

`docker compose -f production.yml run --rm django python manage.py shell`
> To check the logs out, run:

`docker compose -f production.yml logs`
> If you want to scale your application, run:

`docker compose -f production.yml up --scale django=4`

##### Backups
Creating a backup:

`docker compose -f production.yml exec postgres backup`

Listing backups:

`docker compose -f production.yml exec postgres backups`

Restoring a backup:

`docker compose -f production.yml exec postgres restore backup_name.sql.gz`

Removing a backup

`docker compose -f production.yml exec postgres rmbackup backup_name.sql.gz`
