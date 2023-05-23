import json
from datetime import datetime
from functools import wraps

import aiohttp
from nonebot import logger, on_command
from nonebot.adapters.onebot.v11 import ActionFailed, MessageEvent
from nonebot.adapters.onebot.v11.message import Message, MessageSegment
from nonebot.exception import FinishedException
from nonebot.matcher import Matcher
from nonebot.params import CommandArg


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


def format_return_site(ret_site, func=None):
    if not func:
        func = lambda x: x

    msg = f'\n[{(code := ret_site["code"])}]{ret_site["msg"]}'
    if str(code) == "200":
        msg += "\n--------\n" + func(ret_site["data"])
    return msg + "\n--------\nAPI from Me！"

async def get_api_resp_site(name, params, original=False) -> dict | list | bytes:
    async with aiohttp.ClientSession() as s:
        async with s.get(f"https://api.gumengya.com/Api/{name}", params=params) as resp:
            ret_site = f'{None}'
            if original:
                ret_site = await resp.read()
            else:
                ret_site = await resp.json()
            logger.info(f"有人调用了API For Web: {ret_site}")
            #logger.info(f"$.data.{params}")
            return ret_site


def format_json_time(t):
    return (
        datetime.fromisoformat(t.replace("Z", "+00:00"))
        .astimezone()
        .strftime("%Y-%m-%d %H:%M:%S (%Z)")
    )