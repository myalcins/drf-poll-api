# anketOn
. </br>
</br>
# Requirements
</br>
pip3 install -r requirements.txt</br>

# Database
</br>
<ul>
 <li>install postgresql  </li>
 <li>sudo -u postgres -i </li> 
 <li>psql </li>
 <li>create database "db_name"; </li> 
</ul>

# Endpoints
</br><ul>
 <li>api/ question/ [name='question-create'] </li></br>
 <li>api/ question/list/ [name='question-list'] </li></br>
 <li>api/ question/<slug> [name='question-detail'] </li></br>
 <li>api/ vote/ [name='question-vote'] </li></br>
 <li>api/ vote/edit/<int:pk> [name='vote-edit'] </li></br>
 <li>api/ vote/list [name='vote-list'] </li></br>
  </br>
