import pymysql

def get_db_connection():
    connection = pymysql.connect(host='dit_host_navn',
                                 user='dit_brugernavn',
                                 password='din_adgangskode',
                                 db='din_database',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection
