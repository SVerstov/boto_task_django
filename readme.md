# Overview

Testing task for **Boto** company. URL shortener with the ability to edit and delete links.
Option 2. In Django.

Django provides a wealth of ready-made solutions. This is why preparing the second option took less time.

# Installation

## Virtual Environment

It is desirable that `poetry` is already installed in the system.
Install dependencies from **pyproject.toml**.
You can do this with the command `make init` and `make install`.

## Migrations

Apply migrations to create tables:

```
make migrate
```

# Running

```
make run
```
Note: This command launches only DEV server.

After launching, you can view the DRF crud endpoints here:
http://127.0.0.1:8000/api/links/ - for GET all and create new one
http://127.0.0.1:8000/api/links/{link_id} - for update/delete link
http://127.0.0.1:8000/l/{link_id} - redirect link 
# Testing
```
make test
```