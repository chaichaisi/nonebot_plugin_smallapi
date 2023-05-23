from .hander_site import *
@on_command("ip查询", aliases={"IP查询", "IPSOSO"}).handle()
@error_handle()
async def _(matcher: Matcher, args: Message = CommandArg()):
    if not (arg := args.extract_plain_text()):
        await matcher.finish("请输入IP/域名")

    await matcher.finish(
        format_return(
            await get_api_resp("IP", {"ip": arg}),
            lambda ret_web: (
                f'查询目标：{ret_web["ip"]}\n'
                f'IP地址：{ret_web["location"].get("ip")}\n'
                #f'IP类型：{ret_web["location"].get("isp")}\n'
                f'IP地区：{ret_web["location"].get("country")}\n'
                f'IP段起始: {ret_web["location"].get("range").get("start")}\n'
                f'IP段结束: {ret_web["location"].get("range").get("end")}\n'
                f'更多信息：{ret_web["location"].get("area")}'
            ),
        ),
        at_sender=True,
    )
"""
@on_command("网站测速", aliases={"web测速", "WEB测速"}).handle()
@error_handle()
async def _(matcher: Matcher, args: Message = CommandArg()):
    if not (arg := args.extract_plain_text()):
        await matcher.finish("请输入域名")

    await matcher.finish(
        format_return(
            await get_api_resp("speed", {"url": "http://" + arg}),
            lambda ret_web: (
                f'访问速度：{ret_web}'
                ),
        ),
        at_sender=True,
    )
"""


@on_command("ping", aliases={"Ping", "PING"}).handle()
@error_handle()
async def _(matcher: Matcher, args: Message = CommandArg()):
    if not (arg := args.extract_plain_text()):
        await matcher.finish("请输入IP/域名")

    await matcher.finish(
        format_return(
            await get_api_resp("Ping", {"ip": arg}),
            lambda ret_web: (
                f'查询目标：{ret_web["host"]}\n'
                f'IP地址：{ret_web["ip"]}\n'
                f'延迟：{ret_web["ping_avg"]}\n'
                f'主机位置：{ret_web["location"]}\n'
                f'请求节点: {ret_web["node"]}\n'
                #f'主机类型: {ret_web["type"]}\n'
                #f'IP段起始/结束: {ret_web["begin"]}\n{ret_web["end"]}'
                f'更多信息：{ret_web["domain_ip"]}'
            ),
        ),
        at_sender=True,
    )

@on_command("ICP查询", aliases={"icp查询", "Icp查询", "备案查询"}).handle()
@error_handle()
async def _(matcher: Matcher, args: Message = CommandArg()):
    if not (arg := args.extract_plain_text()):
        await matcher.finish("请输入域名")

    await matcher.finish(
        format_return(
            await get_api_resp("ICP", {"domain": arg}),
            lambda ret_web: (
                f'查询域名：{ret_web["domain"]}\n'
                f'网站名称：{ret_web["serviceName"]}\n'
                f'主页地址：{ret_web["homeUrl"]}\n'
                f'主办单位名称：{ret_web["unitName"]}\n'
                f'主办单位性质：{ret_web["class"]}\n'
                f'备案号：{ret_web["icp"]}\n'
                f'备案号名称: {ret_web["mainLicence"]}\n'
                f'更新时间：{ret_web["time"]}'
            ),
        ),
        at_sender=True,
    )

@on_command("拦截检测").handle()
@error_handle()
async def _(matcher: Matcher, args: Message = CommandArg()):
    if not (arg := args.extract_plain_text()):
        await matcher.finish("请输入网址")

    params = {"url": arg}
    qq = await get_api_resp("TencentUrl", params)
    if qq["code"] != 200:
        await matcher.finish(format_return(qq))

    wx = await get_api_resp("WxUrl", params)
    if wx["code"] != 200:
        await matcher.finish(format_return(wx))

    qq["data"]["type"] = wx["data"]["type"]
    await matcher.finish(
        format_return(
            wx,
            lambda ret_web: f'查询网址：{ret_web["url"]}\nQQ/微信拦截状态：{ret_web["type"]}/{ret_web["type"]}',
        ),
        at_sender=True,
    )

@on_command("收录查询").handle()
@error_handle()
async def _(matcher: Matcher, args: Message = CommandArg()):
    if not (arg := args.extract_plain_text()):
        await matcher.finish("请输入域名")

    await matcher.finish(
        format_return(
            await get_api_resp("CheckSEO", {"domain": arg}),
            lambda ret_web: (
                f'查询域名：{ret_web["domain"]}\n'
                f'网站标题：{title if (title := ret_web["title"]) else "未知"}\n'
                f'百度收录量：{ret_web["baidu"]}\n'
                f'好搜收录量：{ret_web["haoso"]}\n'
                f'神马收录量：{ret_web["sm"]}\n'
                f'搜狗收录量：{ret_web["sogou"]}\n'
                f'Bing/必应中国：{ret_web["bing"]}/{ret_web["bingZh"]}\n'
                f'Google：{ret_web["google"]}'
            ),
        ),
        at_sender=True,
    )

@on_command("whois查询", aliases={"Whois查询", "WhoIs查询", "WHOIS查询"}).handle()
@error_handle()
async def _(matcher: Matcher, args: Message = CommandArg()):
    if not (arg := args.extract_plain_text()):
        await matcher.finish("请输入域名")

    await matcher.finish(
        format_return(
            await get_api_resp("Whois", {"domain": arg}),
            lambda ret_web: (
                f'查询域名：{ret_web["domain"]}\n'
                f'注册商：{ret_web["registrar"]}\n'
                f'注册人：{ret_web["registrant"]}\n'
                f'注册邮箱：{ret_web["email"]}\n'
                f'注册时间：{format_json_time(ret_web["registrationTime"])}\n'
                f'到期时间：{format_json_time(ret_web["expirationTime"])}\n'
                f'DNS服务器：{ret_web["nameServer"]}\n'
                #f'域名状态：{", ".join([x["domainState"] for x in ret_web["domainState"]])}\n'
                f'域名状态：{ret_web["domainState"]}\n'
                f'数据更新时间：{ret_web["updateTime"]}'
            ),
        ),
        at_sender=True,
    )