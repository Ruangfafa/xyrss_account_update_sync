import mysql.connector

from app.common.config_loader import AUTH_DB_HOST, AUTH_DB_PORT, AUTH_DB_USER, AUTH_DB_PASSWD, AUTH_DB_DBNAME
from app.common.constant import MysqlServiceCons
from app.service.general_service import generate_offline_uuid
from app.service.logging_service import get_logger

logger = get_logger(MysqlServiceCons.LOGGER)

def get_mysql_conn():
    try:
        conn = mysql.connector.connect(
            host=AUTH_DB_HOST,
            port=AUTH_DB_PORT,
            user=AUTH_DB_USER,
            password=AUTH_DB_PASSWD,
            database=AUTH_DB_DBNAME,
        )
        conn.autocommit = False
        logger.info(MysqlServiceCons.L_S_CONNECT)
        return conn
    except Exception as e:
        logger.exception(MysqlServiceCons.L_F_CONNECT)
        raise

def sync_authme(my_conn, id, r_name, password):
    with my_conn.cursor() as cur:
        cur.execute(MysqlServiceCons.SQL_SYNC_AUTHME, (
            u_name := r_name.lower(),
            r_name,
            password,
            uuid_offline := generate_offline_uuid(u_name),
            id
        ))

        if cur.rowcount == 0:
            cur.execute(MysqlServiceCons.SQL_SYNC_AUTHME_NEW, (
                id, u_name, r_name, password,
                0, 0, 0, MysqlServiceCons.WORLD,
                0, 0, 0, uuid_offline
            ))

def fetch_authme_by_id(my_conn, id):
    with my_conn.cursor(dictionary=True) as cur:
        cur.execute(MysqlServiceCons.SQL_FETCH_AUTHME_BY_ID, (id,))
        return cur.fetchone()
