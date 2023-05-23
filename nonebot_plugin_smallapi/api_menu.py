from nonebot import logger, on_command, on_keyword
from nonebot.matcher import Matcher
from nonebot.adapters.onebot.v11 import MessageSegment, ActionFailed
from nonebot.adapters.onebot.v11 import Bot as OneBot
from nonebot.exception import FinishedException
from pathlib import Path
from functools import wraps

## 定义错误返回
def error_handle():
    def wrapper(func):
        @wraps(func)
        async def decorator(**kwargs):
            try:
                return await func(**kwargs)
            except (ActionFailed, FinishedException):
                raise
            except Exception as e:
                logger.exception("插件菜单出错")
                if matcher := kwargs.get("matcher"):
                    await matcher.finish(f'插件菜单出错，错误信息: {e}')

        return decorator

    return wrapper

## 定义命令触发词
api_pic = on_command("API图片系统", aliases={"api图片系统","图片系统"}, priority=6)
api_text = on_command("API文字系统", aliases={"api文字系统","文字系统"}, priority=6)
api_site = on_command("API站点系统", aliases={"api站点系统","站点系统"}, priority=6)

@api_pic.handle()
@error_handle()
async def handle_onebot(matcher: Matcher,bot: OneBot):
    msg_api_pic = MessageSegment.text(
            "API图片系统\n|次元图|bing图|\n|动漫图|风景图"
        )
    await matcher.finish(msg_api_pic,at_sender=True)

@api_text.handle()
@error_handle()
async def handle_onebot(matcher: Matcher,bot: OneBot):
    msg_api_text = MessageSegment.text(
            "API文字系统\n|舔狗日记|\n|文案|笑话"
        )
    await matcher.finish(msg_api_text,at_sender=True)

@api_site.handle()
@error_handle()
async def handle_onebot(matcher: Matcher,bot: OneBot):
    msg_api_site = MessageSegment.text(
            "API站点系统\n|ip查询|拦截检测|\n|ping|icp查询|\n|whois查询|收录查询|"
        )
    await matcher.finish(msg_api_site,at_sender=True)