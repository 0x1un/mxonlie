from datetime import datetime

from django.db import models

from users.models import UserProfile
from courses.models import Course


# Create your models here.

class UserAsk(models.Model):
    name = models.CharField(max_length=20, verbose_name='name')
    mobile = models.CharField(max_length=11, verbose_name='mobile_num')
    course_name = models.CharField(max_length=50, verbose_name='course_name')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='add_time')

    class Meta:
        verbose_name = 'user_consultation'
        verbose_name_plural = verbose_name


class CourseComments(models.Model):
    # course comments
    user = models.ForeignKey(UserProfile, verbose_name='users')
    course = models.ForeignKey(Course, verbose_name='course')
    comments = models.CharField(max_length=200, verbose_name='comments')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='add_time')

    class Meta:
        verbose_name = 'course_comments'
        verbose_name_plural = verbose_name


class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='users')
    fav_id = models.IntegerField(default=0, verbose_name='data_id')
    fav_type = models.IntegerField(choices=((1, 'Course'), (2, 'Organization'), (3, 'Teacher')), default=1,
                                   verbose_name='favorite_type')

    add_time = models.DateTimeField(default=datetime.now, verbose_name='add_time')

    class Meta:
        verbose_name = 'user_favorites'
        verbose_name_plural = verbose_name


class UserMessage(models.Model):
    user = models.IntegerField(default=0, verbose_name='received_users')
    message = models.CharField(max_length=500, verbose_name='message_contents')
    has_read = models.BooleanField(default=False, verbose_name='has_read_it')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='add_time')

    class Meta:
        verbose_name = 'user_messages'
        verbose_name_plural = verbose_name

class UserCourse(models.Model):
    user = models.IntegerField(default=0, verbose_name='users')
    course = models.ForeignKey(Course, verbose_name='course')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='add_time')

    class Meta:
        verbose_name = 'user_courses'
        verbose_name_plural = verbose_name








