## Installation
 #### 1. Clone the Repository:
    git clone https://github.com/Shirodkar-Shubham-GitHub/Machine_Test
    cd machine_test
 #### 2. Create a Virtual Environment:
    python -m venv my_env
    my_env\Scripts\activate
 #### 3. Install Dependencies:
    pip install -r requirements.txt
 #### 4. Apply Migrations:
    python manage.py migrate
 #### 5. Create a Superuser (for admin access):
    python manage.py createsuperuser
 #### 6. Run the Development Server:
    python manage.py runserver

## Configure MySQL Configuration:
    pip install mysqlclient
#### Setup in settings.py
    DATABASES = {  
    'default': {  
        'ENGINE': 'django.db.backends.mysql',  
        'NAME': 'db_name',  
        'USER': 'db_user',  
        'PASSWORD': 'db_password',  
        'HOST': 'db_host',  
        'PORT': 'db_port',  
        'OPTIONS': {  
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"  
        }  
    }  
    }  
#### Migrations
    python manage.py migrate
