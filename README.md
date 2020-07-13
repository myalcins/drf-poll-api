# anketOn

You can create polls and vote for other user's polls. </br>
</br>
# Requirements
</br>
pip3 install -r requirements.txt</br>
</br>
# Database
</br>
<p>install postgresql </p></br>
---->>> </br>
<p>sudo -u postgres -i </p> </br>
<p>psql </p> </br>
<p>create database "db_name"; </p> </br>
</br>
# Endpoints
</br><ul>
 <li>api/ question/ [name='question-create'] </li></br>
 <li>api/ question/list/ [name='question-list'] </li></br>
 <li>api/ question/<slug> [name='question-detail'] </li></br>
 <li>api/ vote/ [name='question-vote'] </li></br>
 <li>api/ vote/edit/<int:pk> [name='vote-edit'] </li></br>
 <li>api/ vote/list [name='vote-list'] </li></br>
  </br>
