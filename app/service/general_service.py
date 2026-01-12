import uuid

from app.common.constant import GeneralServiceCons


def generate_offline_uuid(name: str) -> str:
    return str(
        uuid.uuid3(
            uuid.NAMESPACE_DNS,
            GeneralServiceCons.OFFLINE_PLAYER + name.lower()
        )
    )

def compare_account(pg_row, my_row) -> bool:
    if my_row is None:
        return False

    id, user_id, mc_name, mc_password = pg_row

    if my_row[GeneralServiceCons.REAL_NAME] != mc_name:
        return False

    if my_row[GeneralServiceCons.PASSWD] != mc_password:
        return False

    if my_row[GeneralServiceCons.UUID_OFFLINE] != generate_offline_uuid(mc_name):
        return False

    return True
