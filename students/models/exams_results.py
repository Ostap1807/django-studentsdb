# -*- coding: utf-8 -*-

from django.db import models

class Exam_result(models.Model):
    """Exam result Model"""

    class Meta(object):
        verbose_name=u'Результати іспиту'
        verbose_name_plural = u'Результати іспитів'

    exam = models.ForeignKey('Exam',
        verbose_name=u'Іспит',
        blank=False)

    student = models.ForeignKey('Student',
        verbose_name=u'Студент',
        blank=False)

    mark = models.IntegerField(
        verbose_name='Бал',
        blank=False)

    def __str__(self):
        return u"%s" % (self.exam)