# anketOn

You can create polls and vote for other user's polls. 

# Requirements

pip3 install -r requirements.txt

# Database

install postgresql
---->>>
sudo -u postgres -i
psql
create database "db_name";
---->>> settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db_name',
        'USER': 'db_username',
        'PASSWORD': 'pass',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# endpoints

api/ question/ [name='question-create']
api/ question/list/ [name='question-list']
api/ question/<slug> [name='question-detail']
api/ vote/ [name='question-vote']
api/ vote/edit/<int:pk> [name='vote-edit']
api/ vote/list [name='vote-list']
  
