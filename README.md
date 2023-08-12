[![Ruff](https://github.com/morheus9/fastapi_postgres_crud/actions/workflows/ruff.yml/badge.svg)](https://github.com/morheus9/fastapi_postgres_crud/actions/workflows/ruff.yml)
[![Pylint](https://github.com/morheus9/fastapi_postgres_crud/actions/workflows/pylint.yml/badge.svg?branch=master)](https://github.com/morheus9/fastapi_postgres_crud/actions/workflows/pylint.yml)
[![DockerCI](https://github.com/morheus9/fastapi_postgres_crud/actions/workflows/push_dockerfile.yml/badge.svg?branch=master)](https://github.com/morheus9/fastapi_postgres_crud/actions/workflows/push_dockerfile.yml)
# This is base CRUD server with postgres and FastApi:
## Just clone, go to /infra and do:
```
cd infra
docker compose up --build
```
## URLs
```
App:          http://127.0.0.1:8000
Docs fastapi: http://127.0.0.1:8000/docs
BD:           http://127.0.0.1:5432
Pg Admin:     http://127.0.0.1:5000
```
### You can make CRUD requests. For example:

- GET All

![Screenshot](images/get_all.png)
![Screenshot](images/_get_all.png)

- GET By ID

![Screenshot](images/get_id.png)
![Screenshot](images/_get_id.png)

- POST

![Screenshot](images/post.png)
![Screenshot](images/_post.png)

- PUT

![Screenshot](images/put.png)
![Screenshot](images/_put.png)

- DELETE

![Screenshot](images/delete.png)
![Screenshot](images/_delete.png)