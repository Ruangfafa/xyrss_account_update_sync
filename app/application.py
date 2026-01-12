from app.common.constant import ApplicationCons
from app.service.general_service import compare_account
from app.service.logging_service import get_logger
from app.service.mysql_service import get_mysql_conn, sync_authme, fetch_authme_by_id
from app.service.postgres_service import get_postgres_conn, fetch_accounts_need_sync, confirm_account_synced

logger = get_logger(ApplicationCons.LOGGER)

def main():
    logger.info(ApplicationCons.L_START)

    pg_conn = None
    my_conn = None

    try:
        pg_conn = get_postgres_conn()
        my_conn = get_mysql_conn()

        logger.info(ApplicationCons.L_S_CONNECT)

        accounts = fetch_accounts_need_sync(pg_conn)
        logger.info(ApplicationCons.L_S_SYNC_ACCOUNTS, len(accounts))

        for row in accounts:
            id, user_id, mc_name, mc_password = row
            logger.info(ApplicationCons.L_SYNCING_ACCOUNT, mc_name)

            try:
                sync_authme(
                    my_conn,
                    id,
                    mc_name,
                    mc_password
                )

                my_row = fetch_authme_by_id(my_conn, id)

                if compare_account(row, my_row):
                    confirm_account_synced(pg_conn, id)
                    pg_conn.commit()
                    my_conn.commit()
                    logger.info(ApplicationCons.L_S_SYNC_ACCOUNT, mc_name)
                else:
                    pg_conn.rollback()
                    my_conn.rollback()
                    logger.warning(ApplicationCons.L_F_COMPARE, mc_name)

            except Exception:
                pg_conn.rollback()
                my_conn.rollback()
                logger.exception(ApplicationCons.L_F_SYNC_ACCOUNT, mc_name)

    except Exception:
        logger.error(ApplicationCons.L_F_SYNC, exc_info=True)

    finally:
        if pg_conn:
            pg_conn.close()
        if my_conn:
            my_conn.close()

if __name__ == ApplicationCons.MAIN_MODULE:
    main()
