from .hander_site import *
@on_command("ip查询", aliases={"IP查询", "IPSOSO"}).handle()
@error_handle()
async def _(matcher: Matcher, args: Message = CommandArg()):
    if not (arg := args.extract_plain_text()):
        await matcher.finish("请输入IP/域名")

    await matcher.finish(
        format_return_site(
            await get_api_resp_site("ip", {"ip": arg}),
            lambda ret_site: (
                #f'查询目标：{ret_site["url"]}\n'
                f'IP地址：{ret_site["address"]}\n'
                f'IP类型：{ret_site["type"]}\n'
                f'IP段起始: {ret_site["begin"]}\n'
                f'IP段结束: {ret_site["end"]}'
                #f'更多信息：{ret_site["domain_ip"]}'
            ),
        ),
        at_sender=True,
    )

@on_command("网站测速", aliases={"web测速", "WEB测速"}).handle()
@error_handle()
async def _(matcher: Matcher, args: Message = CommandArg()):
    if not (arg := args.extract_plain_text()):
        await matcher.finish("请输入域名")

    await matcher.finish(
        format_return_site(
            await get_api_resp_site("speed", {"url": "http://" + arg}),
            lambda ret_site: (
                f'访问速度：{ret_site}'
                ),
        ),
        at_sender=True,
    )





@on_command("ping", aliases={"Ping", "PING"}).handle()
@error_handle()
async def _(matcher: Matcher, args: Message = CommandArg()):
    if not (arg := args.extract_plain_text()):
        await matcher.finish("请输入IP/域名")

    await matcher.finish(
        format_return_site(
            await get_api_resp_site("ping", {"url": arg}),
            lambda ret_site: (
                f'查询目标：{ret_site["url"]}\n'
                f'IP地址：{ret_site["ip"]}\n'
                f'延迟：{ret_site["time"]}\n'
                f'主机位置：{ret_site["address"]}\n'
                f'请求节点: {ret_site["server"]}\n'
                f'主机类型: {ret_site["type"]}\n'
                f'IP段起始/结束: {ret_site["begin"]}\n{ret_site["end"]}'
                #f'更多信息：{ret_site["domain_ip"]}'
            ),
        ),
        at_sender=True,
    )


@on_command("ICP查询", aliases={"icp查询", "Icp查询", "备案查询"}).handle()
@error_handle()
async def _(matcher: Matcher, args: Message = CommandArg()):
    if not (arg := args.extract_plain_text()):
        await matcher.finish("请输入域名")

    #if (await get_api_resp_site("icp", {"domain": arg})) is None:
    #            await matcher.finish(f'icp查询返回为空: 找不到备案信息～')

    else: 
        await matcher.finish(
        format_return_site(
            await get_api_resp_site("icp", {"domain": arg}),
            lambda ret_site: (
                f'查询域名：{ret_site["domain"]}\n'
                #f'网站名称：{ret_site["serviceName"]}\n'
                f'主页地址：{ret_site["domain"]}\n'
                f'主办单位名称：{ret_site["unitName"]}\n'
                f'主办单位性质：{ret_site["natureName"]}\n'
                f'备案号：{ret_site["mainLicence"]}\n{ret_site["serviceLicence"]}\n'
                f'更新时间：{ret_site["updateRecordTime"]}'
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
        format_return_site(
            await get_api_resp_site("whois", {"domain": arg}),
            lambda ret_site: (
                f'查询域名：{ret_site["Domain Name"]}\n'
                f'注册商：{ret_site["Sponsoring Registrar"]}\n'
                f'注册人：{ret_site["Registrant"]}\n'
                f'注册邮箱：{ret_site["Registrant Contact Email"]}\n'
                f'注册时间：{format_json_time(ret_site["Registration Time"])}\n'
                f'到期时间：{format_json_time(ret_site["Expiration Time"])}\n'
                f'DNS服务器：{ret_site["DNS Serve"]}\n'
                #f'域名状态：{", ".join([x["domainState"] for x in ret_site["domainState"]])}\n'
                #f'数据更新时间：{ret_site["updateTime"]}'
            ),
        ),
        at_sender=True,
    )