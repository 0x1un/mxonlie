from datetime import datetime

from django.db import models


# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name='Course Name')
    desc = models.CharField(max_length=300, verbose_name='Course Description')
    detail = models.TextField(verbose_name='Course Detail')
    degree = models.CharField(
        choices=(('primary', 'Primary'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')), max_length=15)
    learn_times = models.IntegerField(default=0, verbose_name='Learn Times(Minutes)')
    students = models.IntegerField(default=0, verbose_name='Students Count')
    fav_nums = models.IntegerField(default=0, verbose_name='Favorite Count')
    image = models.ImageField(upload_to='course/%Y/%m', verbose_name='Cover Pic', max_length=100)
    click_nums = models.IntegerField(default=0, verbose_name='Click Numbers')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='Add Times')

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name='Course')
    name = models.CharField(max_length=100, verbose_name='Chapter Name')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='Add Times')

    class Meta:
        verbose_name = 'Chapter'
        verbose_name_plural = verbose_name


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name='Chapter')
    name = models.CharField(max_length=100, verbose_name='Video_name')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='Add Times')

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = verbose_name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name='Course')
    name = models.CharField(max_length=100, verbose_name='Resource Name')
    download = models.FileField(upload_to='course/resource/%Y/%m', verbose_name='Resource Files', max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='Add Times')

    class Meta:
        verbose_name = 'Course Resource'
        verbose_name_plural = verbose_name
