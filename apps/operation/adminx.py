# -*- coding: utf-8 -*-
__author__ = '0x1un'
__date__ = '11/26/18 10:54 AM'

import xadmin

from .models import UserAsk, UserFavorite, CourseComments, UserMessage, UserCourse

class UserAskAdmin:
    list_display = ['name', 'mobile', 'course_name', 'add_time']
    search_fields = ['name', 'mobile', 'course_name']
    list_filter = ['name', 'mobile', 'course_name']


class UserFavoriteAdmin:
    list_display = ['user', 'fav_id', 'fav_type']
    search_fields = ['user', 'fav_id']
    list_filter = ['user', 'fav_id', 'fav_type']


class CourseCommentsAdmin:
    list_display = ['user', 'course', 'comments', 'add_time']
    search_fields = ['user', 'course', 'comments']
    list_filter = ['user', 'course', 'comments', 'add_time']


class UserMessageAdmin:
    list_display = ['user', 'message', 'has_read', 'add_time']
    search_fields = ['user', 'message', 'has_read']
    list_filter = ['user', 'message', 'has_read', 'add_time']


class UserCourseAdmin:
    list_display = ['user', 'course', 'add_time']
    search_fields = ['user', 'course']
    list_filter = ['user', 'course', 'add_time']


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(CourseComments, CourseCommentsAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)