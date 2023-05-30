from django.db import models
from enums import enum
from django.utils.translation import gettext_lazy as _
from common.validator.validator import validate_uppercase
    
class Course(models.Model):
    id_course = models.AutoField(primary_key=True, unique=True)
    registration_course_id = models.CharField(_('registration course id'), max_length=20, unique=True)
    name_course = models.CharField(_('course name'), unique=True, max_length=45, validators=[validate_uppercase])
    period = models.CharField(_('period'), choices=[(s.name, s.value) for s in enum.Period], max_length=45)
    hour_start = models.TimeField(_('start time'))
    hour_end = models.TimeField(_('end time'))
    area = models.ForeignKey('area.Area', on_delete=models.CASCADE, null=True)
    block = models.ForeignKey('area.Block', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = _('course')
        verbose_name_plural = _('courses')

    def __str__(self):
        return self.name_course