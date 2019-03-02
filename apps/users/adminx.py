# -*- coding: utf-8 -*-
import xadmin
from xadmin import views
from .models import EmailVerifyRecord
from .models import Banner

__author__ = '0x1un'
__date__ = '11/24/18 8:34 PM'


class BaseSetting:
    enable_themes = True
    use_bootswatch = True


xadmin.site.register(views.BaseAdminView, BaseSetting)


class GlobalSettings:
    site_title = 'MxAdmin'
    site_footer = 'MxOnline'
    menu_style = 'accordion'


xadmin.site.register(views.CommAdminView, GlobalSettings)


class EmailVerifyRecordAdmin:
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']


# register the Email to xadmin
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)


class BannerAdmin:
    pass


xadmin.site.register(Banner, BannerAdmin)
