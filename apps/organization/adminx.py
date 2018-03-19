# _*_ encoding: utf-8 _*_
__author__ = 'Jason'
__date__ = '2018/3/18 17:23'

import xadmin

from .models import CityDict, CourseOrg, Teacher


class CityDictAdmin(object):
    list_field = ['name', 'desc', 'add_time']
    filter_field = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']


class CourseOrgAdmin(object):
    list_field = ['name', 'desc', 'click_nums', 'fav_nums', 'image', 'address', 'city', 'add_time']
    filter_field = ['name', 'desc', 'click_nums', 'fav_nums', 'image', 'address', 'city', 'add_time']
    search_fields = ['name', 'desc', 'click_nums', 'fav_nums', 'image', 'address', 'city']


class TeacherAdmin(object):
    list_field = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'add_time']
    filter_field = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'add_time']
    search_fields = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points']


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
