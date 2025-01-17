from django.db import models
from django.utils.translation import gettext_lazy as _
from common.validator.validator import convert_to_uppercase
# gource

class Area(models.Model):
    registration_area_id = models.CharField(
        _('registration area id'),
        max_length=20,
        unique=True,
        null=False,
        blank=False)
    name_area = models.CharField(
        _('name area'),
        max_length=120,
        unique=True,
        null=False,
        blank=False)
    acronym = models.CharField(
        _('acronym'),
        max_length=10,
        unique=True,
        null=False,
        blank=False)
    exchange_area = models.BooleanField(_('exchange area'), default=True)
    is_high_school = models.BooleanField(_('is high school'), default=True)
    blocks = models.ManyToManyField('Blockk', related_name='areas')

    class Meta:
        verbose_name = _('area')
        verbose_name_plural = _('areas')

    def __str__(self):
        return self.name_area

    def get_blocks(self):
        return self.blocks.all()

    def clean(self):
        super().clean()
        convert_to_uppercase(
            self,
            'registration_area_id',
            'name_area',
            'acronym')


class Blockk(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    registration_block_id = models.CharField(
        _('registration block id'),
        max_length=20,
        unique=True,
        null=False,
        blank=False)
    name_block = models.CharField(
        _('name block'),
        max_length=90,
        unique=True,
        null=False,
        blank=False)
    acronym = models.CharField(
        _('acronym'),
        max_length=10,
        unique=True,
        null=False,
        blank=False)

    def __str__(self):
        return self.name_block

    class Meta:
        verbose_name = _('blockk')
        verbose_name_plural = _('blocks')

    def clean(self):
        super().clean()
        convert_to_uppercase(
            self,
            'registration_block_id',
            'name_block',
            'acronym')
