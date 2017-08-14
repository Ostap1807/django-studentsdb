# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

def journal_list(request):
    journal = (
        {
            'id': 1,
            'name': u'Подоба Віталій'},
        {
            'id': 2,
            'name': u'Корост Андрій'},
        {
            'id': 3,
            'name': u'Притула Тарас'},
    )
    return render(request, 'students/journal_list.html', {'journal': journal})

def journal_student(request, sid):
    return HttpResponse('<h1>Journal of student %s</h1>' %sid)

def journal_update(request):
    return HttpResponse('<h1>Journal Update</h1>')