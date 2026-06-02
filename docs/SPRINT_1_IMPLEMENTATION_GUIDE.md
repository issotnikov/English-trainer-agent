# Sprint 1 - Infrastructure

## Цель

Получить рабочий backend.

Definition of Done:

- FastAPI работает
- PostgreSQL подключен
- Alembic работает
- Docker Compose запускается
- Endpoint /health отвечает
- JWT каркас готов

---

# Стек

Python 3.12

FastAPI

SQLAlchemy 2

Alembic

PostgreSQL 16

Redis

Docker

---

# Структура проекта

backend/

app/

api/
core/
db/
models/
schemas/
repositories/
services/
learning/
agents/
prompts/

main.py

---

# Задача 1

Создать структуру каталогов.

---

# Задача 2

Создать Docker Compose.

Сервисы:

- backend
- postgres
- redis

---

# Задача 3

Настроить SQLAlchemy.

Создать:

db/base.py

db/session.py

---

# Задача 4

Настроить Alembic.

Создать первую миграцию.

---

# Задача 5

Создать endpoint.

GET /health

Ответ:

{
  "status": "ok"
}

---

# Задача 6

Создать User model.

Поля:

id

email

hashed_password

created_at

updated_at

---

# Задача 7

Создать JWT infrastructure.

POST /auth/register

POST /auth/login

GET /auth/me

---

# Definition of Done

docker compose up

работает без ошибок

GET /health

возвращает:

{
  "status": "ok"
}