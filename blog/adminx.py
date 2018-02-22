# -*- coding: utf-8 -*-
# from django.contrib import admin
import xadmin
from xadmin import views
from blog.models import Article, Category, Carousel, Nav, Column, News


# class CategoryAdmin(admin.ModelAdmin):
class CategoryAdmin(object):
    search_fields = ('name',)
    list_filter = ('status', 'create_time')
    list_display = ('name', 'parent', 'rank', 'status')
    fields = ('name', 'parent', 'rank', 'status')


# class ArticleAdmin(admin.ModelAdmin):
class ArticleAdmin(object):
    search_fields = ('title', 'summary')
    list_filter = ('status', 'category', 'is_top',
                   'create_time', 'update_time', 'is_top')
    list_display = ('title', 'category', 'author',
                    'status', 'is_top', 'update_time')
    style_fields = {'content':'ueditor'}
    fieldsets = (
        (u'基本信息', {
            'fields': ('title', 'en_title', 'img',
                       'category', 'tags', 'author',
                       'is_top', 'rank', 'status')
            }),
        (u'内容', {
            'fields': ('content',)
            }),
        (u'摘要', {
            'fields': ('summary',)
            }),
        (u'时间', {
            'fields': ('pub_time',)
            }),
    )


# class NewsAdmin(admin.ModelAdmin):
class NewsAdmin(object):
    search_fields = ('title', 'summary')
    list_filter = ('news_from', 'create_time')
    list_display = ('title', 'news_from', 'url', 'create_time')
    fields = ('title', 'news_from', 'url', 'summary', 'pub_time')


# class NavAdmin(admin.ModelAdmin):
class NavAdmin(object):
    search_fields = ('name',)
    list_display = ('name', 'url', 'status', 'create_time')
    list_filter = ('status', 'create_time')
    fields = ('name', 'url', 'status')


# class ColumnAdmin(admin.ModelAdmin):
class ColumnAdmin(object):
    search_fields = ('name',)
    list_display = ('name', 'status', 'create_time')
    list_filter = ('status', 'create_time')
    fields = ('name', 'status', 'article', 'summary')
    filter_horizontal = ('article',)


# class CarouselAdmin(admin.ModelAdmin):
class CarouselAdmin(object):
    search_fields = ('title',)
    list_display = ('title', 'article', 'img', 'create_time')
    list_filter = ('create_time',)
    fields = ('title', 'article', 'img', 'summary')


xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Article, ArticleAdmin)
xadmin.site.register(News, NewsAdmin)
xadmin.site.register(Nav, NavAdmin)
xadmin.site.register(Column, ColumnAdmin)
xadmin.site.register(Carousel, CarouselAdmin)
