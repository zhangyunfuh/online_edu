import xadmin
from users.models import EmailVerifyCode, BannerInfo
from xadmin import views


# 配置xadmin主题，注册时要用到专门的view去注册
class BaseXadminSetting(object):
    enable_themes = True
    use_bootswatch = True


class CommXadminSetting(object):
    site_title = '青枣教育后台管理系统'
    site_footer = '长沙青枣教育培训机构'
    menu_style = 'accordion'


class BannerInfoXadmin(object):  # xadmin注册每一个model
    list_display = ['image', 'url', 'add_time']
    search_fields = ['image', 'url']
    list_filter = ['image', 'url']


class EmailVerifyCodeXadmin(object):
    list_display = ['code', 'email', 'send_type', 'add_time']


xadmin.site.register(BannerInfo, BannerInfoXadmin)
xadmin.site.register(EmailVerifyCode, EmailVerifyCodeXadmin)
xadmin.site.register(views.BaseAdminView, BaseXadminSetting)
xadmin.site.register(views.CommAdminView, CommXadminSetting)
