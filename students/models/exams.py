# -*- coding: utf-8 -*-

from django.db import models

class Exam(models.Model):
    """Exam Model"""

    class Meta(object):
        verbose_name=u'Іспит'
        verbose_name_plural=u'Іспити'

    subject = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Назва предмету")

    lecturer = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Викладач")

    exams_group = models.ForeignKey('Group',
        verbose_name=u'Група',
        blank=False)

    date_of_exam = models.DateTimeField(
        blank=False,
        verbose_name=u'Дата та час проведення')

    notes = models.TextField(
        blank=True,
        verbose_name=u'Додаткові нотатки',
        null=True)

    def __str__(self):
        return u"%s (%s)" % (self.subject, self.exams_group)