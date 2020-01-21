import os
class Config:
    '''
    General configuration class
    '''
    debug = True
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mutumas:Mutuma1234@localhost/blog'
    

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    # MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    

    QUOTES_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
class ProdConfig(Config):
    '''
    Production  configuration class
    '''
    
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    
class DevConfig(Config):
    '''
    Development  configuration class
    '''
    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mutumas:Mutuma1234@localhost/blog'
    DEBUG= True
    ENV = 'development'
    
config_options = {
    'production' : ProdConfig,
    'development' : DevConfig
}