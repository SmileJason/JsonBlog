# -*- coding: utf-8 -*-
# from django.contrib import admin
import xadmin
from xadmin import views
from vmaig_comments.models import Comment


# class CommentAdmin(admin.ModelAdmin):
class CommentAdmin(object):
    search_fields = ('user__username', 'article__title', 'text')
    list_filter = ('create_time',)
    list_display = ('user', 'article', 'text', 'create_time')
    fields = ('user', 'article', 'parent', 'text')

xadmin.site.register(Comment, CommentAdmin)
