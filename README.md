how to run the application:
step 1: Create the environment for application
# using pip 
pip install -r requirements.txt
Or
# using Conda
conda create --name <env_name> --file requirements.txt
step 2: build your tables in database
python manage.py makemigrations
python manage.py migrate
step 3: run your application
python manage.py runserver
