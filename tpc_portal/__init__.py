from .settings import DEV_MODE

if not DEV_MODE:
    import pymysql
    pymysql.install_as_MySQLdb()