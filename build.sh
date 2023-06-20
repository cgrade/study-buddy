pip install -r requirements.txt
pip install djangorestframework
python3.9 manage.py collectstatic
python3 manage.py makemigrations
python3 manage.py migrate
