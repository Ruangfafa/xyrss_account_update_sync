class ApplicationCons:
    LOGGER = "application"

    L_START = "sync start"
    L_S_CONNECT = "database connection OK"
    L_S_SYNC_ACCOUNTS = "accounts need sync: %d"
    L_SYNCING_ACCOUNT = "syncing account %s"
    L_S_SYNC_ACCOUNT = "account %s synced OK"
    L_F_COMPARE = "account %s mismatch, retry later"
    L_F_SYNC_ACCOUNT = "account %s sync failed"
    L_F_SYNC = "sync failed"

    MAIN_MODULE="__main__"

class PostgresServiceCons:
    LOGGER = "postgres_service"

    L_S_CONNECT = "Postgres connected"
    L_F_CONNECT = "Postgres connection failed"

    SQL_FETCH_ACCOUNTS_NEED_SYNC = (
        "SELECT id,user_id,minecraft_name,minecraft_password "
        "FROM public.account "
        "WHERE sync = FALSE"
    )
    SQL_CONFIRM_ACCOUNT_SYNCED = (
        "UPDATE public.account "
        "SET sync = TRUE "
        "WHERE id = %s"
    )

class MysqlServiceCons:
    LOGGER = "mysql_service"
    L_S_CONNECT = "MySQL connected"
    L_F_CONNECT = "MySQL connection failed"

    WORLD = "world"

    SQL_SYNC_AUTHME = (
        "UPDATE xyrss.account "
        "SET "
            "userName = %s, "
            "realName = %s, "
            "password = %s, "
            "uuidOffline = %s "
        "WHERE id = %s"
    )
    SQL_SYNC_AUTHME_NEW = (
        "INSERT INTO xyrss.account ("
            "id, userName, realName, password, "
            "x, y, z, world, "
            "regDate, isLogged, hasSession, uuidOffline"
        ") VALUES ("
            "%s, %s, %s, %s, "
            "%s, %s, %s, %s, "
            "%s, %s, %s, %s"
        ")"
    )
    SQL_FETCH_AUTHME_BY_ID = (
        "SELECT realName, password, uuidOffline "
        "FROM xyrss.account "
        "WHERE id = %s"
    )

class GeneralServiceCons:
    OFFLINE_PLAYER = "OfflinePlayer:"
    REAL_NAME = "realName"
    PASSWD = "password"
    UUID_OFFLINE = "uuidOffline"