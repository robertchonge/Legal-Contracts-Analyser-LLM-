from decouple import config

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', cast=bool, default=False)
OPENAI_API_KEY = config('OPENAI_API_KEY')
