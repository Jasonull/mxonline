# _*_ encoding: utf-8 _*_
__author__ = 'Jason'
__date__ = '2018/3/18 16:37'

import xadmin
from xadmin import views

from .models import Course, Lesson, Video, CourseResource


class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_time', 'students', 'favor', 'image', 'click_nums',
                    'add_time']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_time', 'students', 'favor', 'image', 'click_nums',
                   'add_time']
    search_fields = ['name', 'desc', 'detail', 'degree', 'learn_time', 'students', 'favor', 'image', 'click_nums']


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    list_filter = ['course__name', 'name', 'add_time']
    search_fields = ['course__name', 'name']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    list_filter = ['lesson__name', 'name', 'add_time']
    search_fields = ['lesson__name', 'name']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    list_filter = ['course__name', 'name', 'download', 'add_time']
    search_fields = ['course__name', 'download', 'name']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
