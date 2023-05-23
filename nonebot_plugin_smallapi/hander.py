from nonebot import logger, on_command, on_keyword
from nonebot.matcher import Matcher
from nonebot.adapters.onebot.v11 import Bot as OneBot
from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot.adapters.onebot.v11 import ActionFailed, MessageEvent
from nonebot.adapters.onebot.v11.message import Message, MessageSegment
from nonebot.exception import FinishedException
from nonebot.params import CommandArg
from httpx import AsyncClient
from datetime import datetime
from functools import wraps
from pathlib import Path

import aiohttp
import json
import jsonpath
import ast


def default_parser(args):
    return args.extract_plain_text()

def error_handle():
    def wrapper(func):
        @wraps(func)
        async def decorator(**kwargs):
            try:
                return await func(**kwargs)
            except (ActionFailed, FinishedException):
                raise
            except Exception as e:
                logger.exception("接口访问出错")
                if matcher := kwargs.get("matcher"):
                    await matcher.finish(f'接口访问出错，错误信息: {e}')
        return decorator
    return wrapper

def format_return(ret, func=None):
    if not func:
        func = lambda x: x

    msg = f'\n[{(code := ret["code"])}]{ret["msg"]}'
    if str(code) == "200":
        msg += "\n--------\n" + func(ret["data"])  # MessageSegment拼接
    return msg + "\n--------\nAPI from Me！"

async def get_api_resp(name , params , original=True) -> dict | list | str:
    async with aiohttp.ClientSession() as client:
        ret = f'{None}'
        if original:
            async with client.get(f'https://api.gumengya.com/Api/{name}') as resp:
                ret_old_1 = str(await resp.json())
                ret_old_1 = ast.literal_eval(ret_old_1)
                ret = jsonpath.jsonpath(ret_old_1, f"$.{params}")[0]
                logger.info(f"有人调用了API: {name} {ret_old_1}")
                return ret
        else:
            async with client.get(f'https://api.gumengya.com/Api/{name}') as resp:
                ret = await resp.text()
                logger.info(f"有人调用了API: {name} {ret}")
                return ret