# bookr-dev-test
An ecommerce test exercise.
- project home page serves as the swagger documentation.

# Steps to run project
- clone this repo to your system.
- cd into repo directory.
- Install virtal environment with the below command
```
pip install virtualenv
```
- Create virtal environment with the below command
```
virtualenv venv
```
- Activate virtual environment(venv) if using linux with the below command.
```
source venv/bin/activate
```
- Migrate project with the below command.
```
python manage.py migrate
```
- Make migrations project with the below command.
```
python manage.py makemigrations
```
- run project with command
```
python manage.py ruserver
```
