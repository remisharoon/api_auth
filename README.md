# api_auth
A simple username and password login and registration system using Django REST framework (Python / MySQL)

#Register a new user, using the API

curl -X POST --user remis:remis http://127.0.0.1:8000/users/ -d "{\"username\":\"api_bot", \"email\":\"apibot001@apilabs.com\"}" -H "Content-Type: application/json"

#Query a new user by "id", using the API

curl --user remis:remis http://127.0.0.1:8000/users/3/

#Query a new user by "username", using the API

curl --user remis:remis http://127.0.0.1:8000/users/admin/