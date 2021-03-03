# Setup and Usage Guidelines

This project can be in both dockerized and non-dockerized environments

## Dockerized Environment

1. Create a .env file `touch .env`
2. Copy the contents of the `.env.example` file to the new `.env` file
3. To build the image, Run `docker build -t works_single_view:0.0.1 .`
4. To run migration, Run `docker-compose exec web python manage.py migrate`
5. Run the application `docker-compose up`

## Non-Dockerized Environment

Make sure you have python3, pip3 and postgres installed

1. Create a .env file `touch .env`
2. Copy the contents of the `.env.example` file to the new `.env` file
3. Update the DJANGO_DB_HOST variable from `db` to `localhost` ie `DJANGO_DB_HOST=localhost`
4. Ensure postgres is running. if not run `brew services start postgresql`
5. Install dependencies ie `pip3 install -r requirements.txt`
6. To run migration, Run `python manage.py migrate`
7. Run the application `python manage.py runserver`

## Usage Guidelines

### Matching and reconciling

To match and reconcile metadata, this application has been configured to multiple paths passed through a django command.
For the current sample file located in the root directory, use the following commands for both dockerised and non-dockerised environments

- Run `docker-compose exec web python manage.py ingest works_metadata.csv`
- Run `python manage.py ingest works_metadata.csv`
- To ingest multiple files separate the paths with a space

### Metadata List View
A view has been added where you can see the reconciled data in a tabular format.
Navigate to http://localhost:8001/ for the dockerized environment and http://127.0.0.1:8000/ for the non-dockerized

### Metadata Api View
For the second assignment, the django-rest-framework api view can be accessed on `/api/metadata/<iswc>`
Here is an example call based on the sample provided: http://127.0.0.1:8001/api/metadata/T9204649558

### Admin interface
The django admin interface can be accessed on `/admin` the login credentials can be found in the `.env.example` file