# anketOn

You can create polls and vote for other user's polls. </br>
</br>
# Requirements
</br>
pip3 install -r requirements.txt</br>
</br>
# Database
</br>
install postgresql </br>
---->>> </br>
sudo -u postgres -i </br>
psql </br>
create database "db_name";</br>
---->>> settings.py </br>
DATABASES = { </br>
    'default': { </br>
        'ENGINE': 'django.db.backends.postgresql',</br>
        'NAME': 'db_name',</br>
        'USER': 'db_username',</br>
        'PASSWORD': 'pass',</br>
        'HOST': 'localhost',</br>
        'PORT': '5432',</br>
    }</br>
}</br>
</br>
# endpoints</br>
</br>
api/ question/ [name='question-create']</br>
api/ question/list/ [name='question-list']</br>
api/ question/<slug> [name='question-detail']</br>
api/ vote/ [name='question-vote']</br>
api/ vote/edit/<int:pk> [name='vote-edit']</br>
api/ vote/list [name='vote-list']</br>
  </br>
