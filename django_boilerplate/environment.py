import os
from dotenv import load_dotenv

load_dotenv()

class Environment():
    def __init__(self):
        self.app_env = os.getenv('DJANGO_ENV','development')
        self.app_host = os.getenv('APP_HOST','localhost')
        self.app_port = int (os.getenv('APP_PORT') or 8000)
        self.is_debug = not os.getenv('DJANGO_ENV') == 'production'
        self.allowed_hosts = str(os.getenv('ALLOWED_HOSTS')).strip().split(",")
        self.secret_key = os.getenv('SECRET_KEY')

        # Postgresql Credentials
        self.postgres_db_name = os.getenv('POSTGRES_DB_NAME', 'postgres') 
        self.postgres_host = os.getenv('POSTGRES_HOST', 'localhost')
        self.postgres_port = os.getenv('POSTGRES_PORT', 5432)
        self.postgres_user = os.getenv('POSTGRES_USER', 'postgres')
        self.postgres_pass = os.getenv('POSTGRESS_PASS', 'admin')

config = Environment()
