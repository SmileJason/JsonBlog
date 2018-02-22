# -*- coding: utf-8 -*-
# from django.contrib import admin
import xadmin
from xadmin import views
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from vmaig_auth.models import VmaigUser
from vmaig_auth.forms import VmaigUserCreationForm


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True
 
xadmin.site.register(views.BaseAdminView, BaseSetting)

class GlobalSetting(object):
    site_title = "Json Blog"
    site_footer = "https://blog.json666.cn/xadmin"
    menu_style = "accordion"
    # global_search_models = [V_UserInfo, UserDistrict]
    # global_models_icon = {
    #     V_UserInfo: "glyphicon glyphicon-user", UserDistrict: "fa fa-cloud"
    # }
 
xadmin.site.register(views.CommAdminView, GlobalSetting)

# class VmaigUserAdmin(UserAdmin):
class VmaigUserAdmin(object):
    add_form = VmaigUserCreationForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2')
        }),
    )
    fieldsets = (
        (u'基本信息', {'fields': ('username', 'password', 'email')}),
        (u'权限', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (u'时间信息', {'fields': ('last_login', 'date_joined')}),
    )

xadmin.site.unregister(Group)
# xadmin.site.register(VmaigUser, VmaigUserAdmin)
