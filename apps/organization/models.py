from datetime import datetime

from django.db import models


# Create your models here.

class CityDict(models.Model):
    name = models.CharField(max_length=20, verbose_name='city_name')
    desc = models.CharField(max_length=200, verbose_name='description')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='add_time')

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = verbose_name


class CourseOrg(models.Model):
    name = models.CharField(max_length=50, verbose_name='org_name')
    desc = models.TextField(verbose_name='org_description')
    click_nums = models.IntegerField(default=0, verbose_name='click_numbers')
    fav_nums = models.IntegerField(default=0, verbose_name='favorite_nums')
    image = models.ImageField(upload_to='org/%Y/%m', verbose_name='cover_pic', max_length=100)
    address = models.CharField(max_length=150, verbose_name='org_locations')
    city = models.ForeignKey(CityDict, verbose_name='AtTheCity')

    class Meta:
        verbose_name = 'Course_Organization'
        verbose_name_plural = verbose_name


class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg, verbose_name='AtTheOrganization')
    name = models.CharField(max_length=50, verbose_name='teacher_name')
    work_years = models.IntegerField(default=0, verbose_name='work_years')
    work_company = models.CharField(max_length=50, verbose_name='working_company')
    work_position = models.CharField(max_length=50, verbose_name='working_position')
    points = models.CharField(max_length=50, verbose_name='teaching_posts')
    fav_nums = models.IntegerField(default=0, verbose_name='favorite_nums')
    click_nums = models.IntegerField(default=0, verbose_name='click_nums')
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = 'Teachers'
        verbose_name_plural = verbose_name
