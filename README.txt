Stack used:

Django
Django Rest Framework
Mysql

---------------------------------------

Installation 

1) Install the below packages using apt-get.

- mysql-server       (Note: Please set the password as root123, and create DB instadb)
- libmysqlclient-dev
- virtualenv

2) Create a python virtualenv and activate the same

 # virtualenv benv
 # source benv/bin/activate

3) Install all packages using requirements.txt

# pip install -r requirements.txt

4) Go to the folder and run migrate to run migrations

# cd freno
# python manage.py migrate

5) Run the application using below command

# python manage.py runserver

-----------------------------------------------------------------


Create / Edit / Delete / Retrieve / List operations

Open another tab to run the below commands while the django application runs in the other tab.

List all team members

# curl -X GET -H "Content-Type:application/json" http://127.0.0.1:8000/api/team/list-or-create-member/


Create team member

# curl -X POST -H "Content-Type:application/json" http://127.0.0.1:8000/api/team/list-or-create-member/ -d '{"first_name": "David", "last_name": "Jones", "phone": "+15101234567", "email": "test123@test.com", "is_admin": 0}'


Get a team member details

# curl -X GET -H "Content-Type:application/json" http://127.0.0.1:8000/api/team/member/1/


Edit team member details

# curl -X PUT -H "Content-Type:application/json" http://127.0.0.1:8000/api/team/member/1/ -d '{"first_name": "Davidedittttttttt", "email": "testEDIT@test.com", "is_admin": 0}'


Delete a team member

# curl -X DELETE -H "Content-Type:application/json" http://127.0.0.1:8000/api/team/member/2/


---------------------------------------------------------

