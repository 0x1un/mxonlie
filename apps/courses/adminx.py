# -*- coding: utf-8 -*-
__author__ = '0x1un'
__date__ = '11/25/18 6:33 PM'

from .models import Course, Video, Lesson, CourseResource
import xadmin


class CourseAdmin:
    list_display = [
        'name', 'desc', 'detail', 'degree', 'learn_times',
        'students', 'fav_nums', 'image', 'click_nums', 'add_time',
    ]
    search_fields = [
        'name', 'desc', 'detail', 'degree', 'learn_times',
        'students', 'fav_nums', 'image', 'click_nums', 'add_time',
    ]
    list_filter = [
        'name', 'desc', 'detail', 'degree', 'learn_times',
        'students', 'fav_nums', 'image', 'click_nums',
    ]


xadmin.site.register(Course, CourseAdmin)


#
# class VideoAdmin:
#     pass
#
#
class LessonAdmin:
    list_display = [
        'course', 'name', 'add_time'
    ]
    search_fields = [
        'course', 'name'
    ]
    list_filter = [
        'course__name', 'name', 'add_time'
    ]


xadmin.site.register(Lesson, LessonAdmin)


class CourseResourceAdmin:
    list_display = ['course', 'name', 'download', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course', 'name', 'download', 'add_time']


xadmin.site.register(CourseResource, CourseResourceAdmin)
