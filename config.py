#coding=utf-8
import os


if 'SERVER_SOFTWARE' in os.environ:
    import sae.const
    class SAEConfig(object):
        MYSQL_HOST = sae.const.MYSQL_HOST
        MYSQL_PORT =sae.const.MYSQL_PORT
        MYSQL_USER =sae.const.MYSQL_USER
        MYSQL_PASS =sae.const.MYSQL_PASS
        MYSQL_DB =sae.const.MYSQL_DB
        MYSQL_HOST_S = sae.const.MYSQL_HOST_S
        SECRET_KEY = "12345"
        SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@%s:%s/%s?charset=utf8' %\
                (MYSQL_USER, MYSQL_PASS, MYSQL_HOST, MYSQL_PORT, MYSQL_DB)
        DEBUG = True
        TESTING = False

    CurrentConfig = SAEConfig
else:
    class DevelopmentConfig(object):
        MYSQL_HOST = 'localhost'
        MYSQL_PORT = '3306'
        #MYSQL_USER = os.environ['LOGNAME']
        MYSQL_USER = "wwb"
        MYSQL_PASS = ''
        MYSQL_DB = 'autumn'
        SECRET_KEY = ""
        SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@%s:%s/%s?charset=utf8' %\
                (MYSQL_USER, MYSQL_PASS, MYSQL_HOST, MYSQL_PORT, MYSQL_DB)
        DEBUG = False
        TESTING = False


    CurrentConfig = DevelopmentConfig
