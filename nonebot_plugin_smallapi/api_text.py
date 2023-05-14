from .hander import *
text_tgrj = on_command("舔狗日记", priority=3)

text_wenan = on_command("文案", priority=3)

text_xh = on_command("笑话" ,priority=3)

@text_tgrj.handle()
@error_handle()
async def handle_onebot(bot: OneBot, matcher: Matcher, args: Message = CommandArg()):
    await matcher.finish(
        format_return(
            {
                "code": "200",
                "msg": "请求成功",
                "data": MessageSegment.text(
                    await get_api_resp("dog" , "data" , original=True)
                ),
            },
            lambda ret: ret,
        ),
        at_sender=True,
    )

@text_wenan.handle()
@error_handle()
async def handle_onebot(matcher: Matcher, args: Message = CommandArg()):
    await matcher.finish(
        format_return(
            {
                "code": "200",
                "msg": "请求成功",
                "data": MessageSegment.text(
                    await get_api_resp("renjian" , "data" , original=True)
                ),
            },
            lambda ret: ret,
        ),
        at_sender=True,
    )

@text_xh.handle()
@error_handle()
async def handle_onebot(matcher: Matcher, args: Message = CommandArg()):
    await matcher.finish(
        format_return(
            {
                "code": "200",
                "msg": "请求成功",
                "data": MessageSegment.text(
                    await get_api_resp("aiqinggongyu" , "data" , original=True)
                ),
            },
            lambda ret: ret,
        ),
        at_sender=True,
    )