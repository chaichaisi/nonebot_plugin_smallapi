from .hander import *
pic_ecy = on_command("次元图", priority=6)

pic_dm = on_command("动漫图", priority=6)

pic_bing = on_command("Bing图", aliases={"bing图"} , priority=6)

pic_fj = on_command("风景图", priority=6)

@pic_ecy.handle()
@error_handle()
async def handle_onebot(bot: OneBot, matcher: Matcher, args: Message = CommandArg()):
    await matcher.finish(
        format_return(
            {
                "code": "200",
                "msg": "请求成功",
                "data": MessageSegment.image(
                    await get_api_resp("DmImg" , "data.url" , original=True)
                ),
            },
            lambda ret: ret,
        ),
        at_sender=True,
    )

@pic_dm.handle()
@error_handle()
async def handle_onebot(bot: OneBot, matcher: Matcher, args: Message = CommandArg()):
    await matcher.finish(
        format_return(
            {
                "code": "200",
                "msg": "请求成功",
                "data": MessageSegment.image(
                    await get_api_resp("DmImgS" , "data.url" , original=True)
                ),
            },
            lambda ret: ret,
        ),
        at_sender=True,
    )

@pic_bing.handle()
@error_handle()
async def handle_onebot(bot: OneBot, matcher: Matcher, args: Message = CommandArg()):
    await matcher.finish(
        format_return(
            {
                "code": "200",
                "msg": "请求成功",
                "data": MessageSegment.image(
                    await get_api_resp("BingImg" , "data.url" , original=True)
                ),
            },
            lambda ret: ret,
        ),
        at_sender=True,
    )

@pic_fj.handle()
@error_handle()
async def handle_onebot(bot: OneBot, matcher: Matcher, args: Message = CommandArg()):
    await matcher.finish(
        format_return(
            {
                "code": "200",
                "msg": "请求成功",
                "data": MessageSegment.image(
                    await get_api_resp("FjImg" , "data.url" , original=True)
                ),
            },
            lambda ret: ret,
        ),
        at_sender=True,
    )