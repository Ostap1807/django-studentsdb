# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms import ModelForm
from django.views.generic import UpdateView, DeleteView, CreateView

from ..models import Student, Group, Exam, Exam_result

def exams_list(request):
    exams = Exam.objects.all()

    # try to order students list
    order_by = request.GET.get('order_by', '')
    if order_by in ('id', 'subject', 'exams_group',
                    'lecturer', 'date_of_exam'):
        exams = exams.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            exams = exams.reverse()

    # paginate students
    paginator = Paginator(exams, 3)
    page = request.GET.get('page')
    try:
        exams = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page
        exams = paginator.page(1)
    except EmptyPage:
        # If result is out of range (e.g. 9999), deliver
        # last page of results
        exams = paginator.page(paginator.num_pages)

    return render(request, 'students/exams_list.html',
                  {'exams': exams})

def exams_add(request):
    # was form posted?
    if request.method == "POST":
        # was form add button clicked?
        if request.POST.get('add_button') is not None:
            # errors collection
            errors = {}

            # data for exam object
            data = {'notes': request.POST.get('notes')}

            # validate user input
            subject = request.POST.get('subject', '').strip()
            if not subject:
                errors['subject'] = u"Предмет є обов'язковим"
            else:
                data['subject'] = subject

            lecturer = request.POST.get('lecturer', '').strip()
            if not lecturer:
                errors['lecturer'] = u"Викладач є обов'язковим"
            else:
                data['lecturer'] = lecturer

            exams_group = request.POST.get('exams_group', '').strip()
            if not exams_group:
                errors['exams_group'] = u"Оберіть групу для екзамену"
            else:
                groups = Group.objects.filter(pk=exams_group)
                if len(groups) != 1:
                    errors['exams_group'] = u"Оберіть коректну групу"
                else:
                    data['exams_group'] = groups[0]

            date_of_exam = request.POST.get('date_of_exam', '').strip()
            if not date_of_exam:
                errors['date_of_exam'] = u"Дата екзамену є обов'язковою"
            else:
                # try:
                #     datetime.strptime(date_of_exam, '%Y-%m-%d %H:%M')
                # except Exception:
                #     errors['date_of_exam'] = \
                #         u"Введіть коректний формат дати (напр. 2017-07-12 15:45)"
                # else:
                data['date_of_exam'] = date_of_exam

            # save exam
            if not errors:
                exam = Exam(**data)
                exam.save()

                # redirect to exams list
                return HttpResponseRedirect(
                    u'%s?status_message=Іспит успішно додано!' %
                    reverse('exams'))
            else:
                # render form with errors and previous user input
                return render(request, 'students/exams_add.html',
                    {'groups': Group.objects.all().order_by('title'),
                     'errors': errors})
        elif request.POST.get('cancel_button') is not None:
            # redirect to exam page on cancel button
            return HttpResponseRedirect(
                u'%s?status_message=Додавання іспиту скасовано!' %
                reverse('exams'))
    else:
        # initial form render
        return render(request, 'students/exams_add.html',
            {'groups': Group.objects.all().order_by('title')})

def exams_result(request, gid):
    results_list = Exam_result.objects.filter(exam__exams_group__pk='%s' % gid)
    return render(request, 'students/exams_results.html', {'results_list': results_list})

def exams_result_add(request):
    return HttpResponse('<h1>Exams result adding form</h1>')
