#Login-SSH
Usage:
```batch
python3 ssh_login <IP_TARGET> -u username.txt -p password.txt
```
#Scan Port
Usage:
```batch
python3 scan1.py <IP_TARGET>
```
## Create user
```
CREATE USER 'user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'your_password';
```

## If your account lock
```
ALTER USER 'apt3233'@'localhost' ACCOUNT UNLOCK;
```

## Show user
```
SELECT User, Host FROM mysql.user;
```

## Show all databse 
```
SHOW DATABASES
```

## Create Database
```
CREATE DATABASE name_db;
```
- Use database ```USE name_db```
- Remove database ```DROP DATABASE name_db```
- Show all databse ```SHOW DATABASES```
