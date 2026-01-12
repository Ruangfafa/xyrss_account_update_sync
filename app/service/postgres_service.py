import psycopg2

from app.common.config_loader import SUPA_DB_HOST, SUPA_DB_PORT, SUPA_DB_USER, SUPA_DB_PASSWD, SUPA_DB_DBNAME
from app.common.constant import PostgresServiceCons
from app.service.logging_service import get_logger

logger = get_logger(PostgresServiceCons.LOGGER)

def get_postgres_conn():
    try:
        conn = psycopg2.connect(
            host=SUPA_DB_HOST,
            port=SUPA_DB_PORT,
            user=SUPA_DB_USER,
            password=SUPA_DB_PASSWD,
            dbname=SUPA_DB_DBNAME,
        )
        conn.autocommit = False
        logger.info(PostgresServiceCons.L_S_CONNECT)
        return conn
    except Exception as e:
        logger.exception(PostgresServiceCons.L_F_CONNECT)
        raise

def fetch_accounts_need_sync(pg_conn):
    with pg_conn.cursor() as cur:
        cur.execute(PostgresServiceCons.SQL_FETCH_ACCOUNTS_NEED_SYNC)
        return cur.fetchall()

def confirm_account_synced(pg_conn, id):
    with pg_conn.cursor() as cur:
        cur.execute(PostgresServiceCons.SQL_CONFIRM_ACCOUNT_SYNCED, (id,))