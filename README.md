# Libro Smart

[video instruction](https://www.youtube.com/watch?v=Fx3q4xp_Ey8) 


## Setup

### Clone project

```bash
git clone https://github.com/azizjon-aliev/LibroSmart.git
```

### Copy the .env.example file as .env and set values to empty fields 

```bash 
cp .env.example .env
```

### Run with docker compose:

```bash
docker compose up -d
```

### Run without docker compose:

#### Add virtualenv

```bash
python -m venv venv
```

#### Activate virtualenv

```bash
source venv/bin/activate
```

#### Install requirements

```bash
pip install -r requirements.txt
```

#### Run migrations

```bash
python manage.py migrate
```

#### Create superuser

```bash
python manage.py init_admin
```

#### Run project

```bash
python manage.py runserver
```

### API Documentation

```bash
http://localhost/swagger/
```

### Admin

```bash
http://localhost/admin/
```

### Data for login

##### Username - admin

##### Password - admin

