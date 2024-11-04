import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'nunca-adivinaras'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    

    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'calubrossy@gmail.com'
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'Calo'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'Calo111'
    ADMINS = ['calubrossy@gmail.com']
    POSTS_PER_PAGE = 25   
    LENGUAGES = ['es', 'en']