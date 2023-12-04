import os


BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# postgres config
DATABASE_URI = 'postgresql://postgres:postgres@localhost/' + 'auth_system'

SECRET_KEY = "BMepvE4aNVzLsu1ziHTKi8fNJdBLoL04Si"

JWT_EXPIRE = 60 * 60
