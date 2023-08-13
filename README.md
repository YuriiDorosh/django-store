touch .env

python3 -m venv env

source env/bin/activate

pip3 install -r requirements.txt

python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py loaddata products/fixtures/categories.json

python3 manage.py loaddata products/fixtures/goods.json

python3 manage.py createsuperuser

python3 manage.py runserver
