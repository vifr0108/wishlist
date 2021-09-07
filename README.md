# Wishlist django project

## Development. Step by step
Start project
- startproject (name wishlist) - create project
- startapp (name main) - create application

Create Model
- describe models.py
- makemigrations main - create instration for migrate to DB
- migrate main

Create admin console for work with db
- createsuperuser - create superuser
- go to http://127.0.0.1:8000/admin

## Testing
- runserver
- go to http://127.0.0.1:8000/

Configure settings.py
- add main to INSTALLED_APPS 
- SECRET_KEY move to .env file
