import os
basedir = os.path.abspath(os.path.dirname(__file__))

class iceConfig:
    ICE_CONF = '/dsserver/dsserver.conf'
    DB_ACCOUNT_IP = "db_account_ip"
    DEF_DB_IP = '127.0.0.1'
    DB_ACCOUNT_PORT = 'db_account_port'
    DEF_DB_PORT = 3306
    DB_NAME = 'db_name'
    DEF_DB_NAME = 'ijdbs'
    DB_USER = 'db_user'
    DEF_DB_USER = 'ijmaster'
    DB_PASS = 'db_pass'
    DEF_DB_PASS = 'ijjazhang'

def getcconf_value(key):
    with open(iceConfig.ICE_CONF, "rb") as f:
        for l in f.readlines():
            line = l.strip()
            is_started = line.startswith(key)
            if is_started == False:
                continue
            kend = len(key)
            line = line[len(key):].strip()
            if line[0] != '=':
                continue
            return line[1:]
    return None

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass

    @classmethod
    def init(cls):
        u = getcconf_value(iceConfig.DB_USER) or iceConfig.DEF_DB_USER
        p = getcconf_value(iceConfig.DB_PASS) or iceConfig.DEF_DB_PASS
        db_ip = getcconf_value(iceConfig.DB_ACCOUNT_IP) or iceConfig.DEF_DB_IP
        db_port = getcconf_value(iceConfig.DB_ACCOUNT_PORT) or iceConfig.DEF_DB_PORT
        db_name = getcconf_value(iceConfig.DB_NAME) or iceConfig.DEF_DB_NAME
        mysql_url = 'mysql://%s:%s@%s:%s/%s?charset=utf8' % (u, p, db_ip, db_port, db_name)
        cls.SQLALCHEMY_DATABASE_URI = mysql_url

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = 'mysql://ijmaster:ijjazhang@10.135.255.201:3306/ijdbs?charset=utf8'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql://ijmaster:ijjazhang@10.135.255.201:3306/ijdbs?charset=utf8'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://ijmaster:ijjazhang@10.135.255.201:3306/ijdbs?charset=utf8'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
