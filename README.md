# Weather Data Reader from UK MetOffice

This app takes region and parameter values as inputs and serves weather data in JSON format from UK MetOffice.

## Prerequisites

### Docker Compose

Docker(-compose) is required. Please click [here](https://docs.docker.com/install/) for more information.

## Installation

The settings are controlled by environment variables. For development, the `docker-compose.yml` uses an environment file which must be created first:

```bash
cp .env.dist .env
```

After that edit `.env` and update the settings, if any.

Then run `docker-compose up -d` and the app is available under [http://localhost:8000](http://localhost:8000).

For the first run, we need to migrate the database:
```
docker-compose exec web python manage.py migrate
```

And create a superuser
```
docker-compose exec web python manage.py createsuperuser
```

## Configuration

Like written under Installation, the environment file could/must have following variables:

```
SECRET_KEY
DEBUG
POSTGRES_USER
POSTGRES_DB
POSTGRES_PASSWORD
POSTGRES_HOST
POSTGRES_PORT
ENV_NAME
```

Normal code changes dont require a relaunch of the containers. Any changes in local **ENV** file need a restart with `docker-compose down` and `docker-compose up -d`. Logs can be shown with `docker-compose logs -f`.

## Usage

This application uses token based authentication. Hence to interact with weather api first, a token is required.
Token can be generated by [http://localhost:8000/api-token-auth/](http://localhost:8000/api-token-auth/) by 
sending params `username` and `password` as a ```POST``` request.
After token is generated, API can be accessed on [http://localhost:8000/api/weather/](http://localhost:8000/api/weather/) by sending a ```GET``` request with params `region` and `parameter`.

## Running Tests and coverage report

```
docker-compose exec web pytest --isort --flake8 --cov -vs .
```