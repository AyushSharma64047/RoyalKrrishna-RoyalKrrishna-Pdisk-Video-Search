# (c) @RoyalKrrishna

from core.login import vivdisk_login

vivisk_DB = {}

async def get_cookies(email: str, password: str) -> str:

    if not vivdisk_DB:

        user_id, cookies = await vivdisk_login(email, password)

        vivdisk_DB["cookies"] = cookies

        vivdisk_DB["user_id"] = user_id

        vivdisk_DB["email"] = email

        vivdisk_DB["password"] = password

    return vivdisk_DB["cookies"]

async def set_cookies(data: dict):

    vivdisk_DB["email"] = data["email"]

    vivdisk_DB["password"] = data["password"]

    vivdisk_DB["user_id"] = data["user_id"]

    vivdisk_DB["cookies"] = data["cookies"]

