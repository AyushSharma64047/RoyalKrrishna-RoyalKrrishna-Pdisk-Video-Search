# (c) @RoyalKrrishna

import requests
from urllib import parse
from typing import Union
from core.get_cookies import (
    get_cookies,
    set_cookies
)
from core.login import vivdisk_login

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
search_api = "https://vivdisk.com/search.php?api=d16088fc465567b77c4fa26e2c3781d5dc63ca64#dDirName=true"


async def search_vivdisk_videos(query: str, email: str, password: str) -> Union[dict, Exception]:
    try:
        cookies = await get_cookies(username, password)
        response = requests.get(search_api.format(parse.quote(query)), cookies={"Cookie": cookies}, headers={"User-Agent": user_agent})
        data = response.json()
        if data["msg"] == "Please login again":
            user_id, cookies = await vivdisk_login(username, password)
            await set_cookies({
                "username": email,
                "password": password,
                "user_id": user_id,
                "cookies": cookies
            })
            return await search_vivdisk_videos(query, username, password)
        else:
            return data
    except Exception as error:
        print(error)
        return error
