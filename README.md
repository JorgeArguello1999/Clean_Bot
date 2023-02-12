# Telegram Clean Bot

## ¿Qué es?
Telegram Bot es un pequeño proyecto cerado con la finalidad de realizar un seguimiento de las personas que deben realizar la limpieza de mi curso.

## Dependencias
- python-telegram-bot v.13.0
- pymongo

## Docker
```sh
docker run -d --name Tel_Bot -e MONGO_INITDB_ROOT_USERNAME=db_user -e MONGO_INITDB_ROOT_PASSWORD=db_admin -p 27017:27017 mongo
```