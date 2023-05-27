from django.db import models
from enums import enum 
from django.utils.translation import gettext_lazy as _

class Attribution_preference(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)

class Preference_schedule(models.Model):
    attribution_preference = models.ForeignKey('Attribution_preference', on_delete=models.CASCADE)
    timeslot = models.ForeignKey('timetable.Timeslot', on_delete=models.CASCADE)
    day = models.CharField(_('day'), choices=[(s.name, s.value) for s in enum.Day], max_length=45) 

class Teaching_support_activity_attribution(models.Model):
    attribution_preference = models.ForeignKey('Attribution_preference', on_delete=models.CASCADE)

class Teaching_support_activity(models.Model):
    name = models.CharField(_('name'), max_length=45)
    duration = models.TimeField(_('duration'))

class Attribution_workload_supplementation(models.Model):
    attribution_preference = models.ForeignKey('Attribution_preference', on_delete=models.CASCADE)
    workload_supplementation = models.ForeignKey('Workload_supplementation', on_delete=models.CASCADE)

class Workload_supplementation(models.Model):
    name = models.CharField(_('name'), max_length=45)
    duration = models.TimeField(_('duration'))

class Attribution_preference_course_preference(models.Model):
    attribution_preference = models.ForeignKey('Attribution_preference', on_delete=models.CASCADE)
    course_preference = models.ForeignKey('Course_preference', on_delete=models.CASCADE)

class Course_preference(models.Model):
    course = models.ForeignKey('course.Course', on_delete=models.CASCADE)
    count_course = models.IntegerField(_('count course'))
    priority = models.CharField(_('day'), choices=[(s.name, s.value) for s in enum.Priority], max_length=45)
    period = models.CharField(_('period'), choices=[(s.name, s.value) for s in enum.Period], max_length=45)
