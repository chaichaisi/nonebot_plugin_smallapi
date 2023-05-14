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
                    await get_api_resp("randomAcgPic?type=pc" , "data" , original=True)
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
                    await get_api_resp("random4kPic?type=acg" , "data" , original=True)
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
                    await get_api_resp("bing" , "data" , original=True)
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
                    await get_api_resp("random4kPic?type=wallpaper" , "data" , original=True)
                ),
            },
            lambda ret: ret,
        ),
        at_sender=True,
    )