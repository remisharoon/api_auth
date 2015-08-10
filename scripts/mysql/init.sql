mysql -u root

create database dj_api_auth;
CREATE USER 'dj_api'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON * . * TO 'dj_api'@'localhost';