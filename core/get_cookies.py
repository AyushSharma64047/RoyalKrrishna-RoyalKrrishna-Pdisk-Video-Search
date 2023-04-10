# (c) @RoyalKrrishna

from core.login import VIVdisk_login

VIVDisk_DB = {}

async def get_cookies(username: str, password: str) -> str:

    if not PDisk_DB:

        user_id, cookies = await pdisk_login(username, password)

        VIVDisk_DB["cookies"] = cookies

        VIVDisk_DB["user_id"] = user_id

        VIVDisk_DB["username"] = username

        VIVDisk_DB["password"] = password

    return PDisk_DB["cookies"]

async def set_cookies(data: dict):

    VIVDisk_DB["username"] = data["username"]

    VIVDisk_DB["password"] = data["password"]

    VIVDisk_DB["user_id"] = data["user_id"]

    VIVDisk_DB["cookies"] = data["cookies"]

