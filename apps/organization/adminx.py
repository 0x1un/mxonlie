# -*- coding: utf-8 -*-
__author__ = '0x1un'
__date__ = '11/25/18 6:28 PM'

import xadmin
from .models import CityDict, CourseOrg, Teacher


class CityDictAdmin:
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc']


xadmin.site.register(CityDict, CityDictAdmin)


class CourseOrgAdmin:
    list_display = ['name', 'desc', 'click_nums', 'fav_nums', 'image', 'address', 'city']
    search_fields = ['name', 'desc', 'city', 'address', 'fav_nums', 'click_nums']
    list_filter = ['name', 'desc', 'city', 'address', 'fav_nums', 'click_nums']


xadmin.site.register(CourseOrg, CourseOrgAdmin)


class TeacherAdmin:
    list_display = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'fav_nums', 'click_nums',
                    'add_time']
    search_fields = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'fav_nums', 'click_nums']
    list_filter = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'fav_nums', 'click_nums',
                   'add_time']


xadmin.site.register(Teacher, TeacherAdmin)
