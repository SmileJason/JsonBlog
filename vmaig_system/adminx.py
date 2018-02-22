# from django.contrib import admin
import xadmin
from xadmin import views
from vmaig_system.models import Notification, Link

# Register your models here.


# class NotificationAdmin(admin.ModelAdmin):
class NotificationAdmin(object):
    search_fields = ('text',)
    list_display = ('title', 'from_user', 'to_user', 'create_time')
    list_filter = ('create_time',)
    fields = ('title', 'is_read', 'text',
              'url', 'from_user', 'to_user', 'type')


# class LinkAdmin(admin.ModelAdmin):
class LinkAdmin(object):
    search_fields = ('title',)
    list_display = ('title', 'url')
    list_filter = ('create_time',)
    fields = ('title', 'url', 'type')


xadmin.site.register(Notification, NotificationAdmin)
xadmin.site.register(Link, LinkAdmin)
