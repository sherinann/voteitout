import os

class Config(object):
    SECRET_KEY=os.environ.get('SECRET_KEY') or 'buhahahaha'
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:root@localhost/voteitout'
    SQLALCHEMY_TRACK_MODIFICATIONS = True