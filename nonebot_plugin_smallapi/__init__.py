from nonebot.plugin import PluginMetadata
from .api_menu import *
from .api_pic import *
from .api_text import *
from .api_site import *
logger.success(f"小小API调用插件跑起来喽～")

__plugin_meta__ = PluginMetadata(
    name="小小API调用插件",
    description="调用api来操福Q民～",
    usage="发送“API图片/文字/站点系统”查看",
    extra={
        "unique_name": "smallapi",
        "author": "Chaichaisi <chaichaisi@qq.com>",
        "version": "0.0.1",
    },
)