# pokemon_battle_simulator

make the virtual environment and intall all dependancy from requirements.txt

in this before run the project system requires redis 

before start run command
    python manage.py migrate
        then
    python manage.py runserver


in another to run the celery use command
    celery -A battle_simulator  worker -l info -P eventlet
