# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms import ModelForm
from django.views.generic import UpdateView, DeleteView, CreateView

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions

from ..models import Student, Group

def groups_list(request):
    groups = Group.objects.all()

    # try to order students list
    order_by = request.GET.get('order_by', '')
    if order_by in ('id', 'title'):
        groups = groups.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            groups = groups.reverse()

    # paginate students
    paginator = Paginator(groups, 3)
    page = request.GET.get('page')
    try:
        groups = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page
        groups = paginator.page(1)
    except EmptyPage:
        # If result is out of range (e.g. 9999), deliver
        # last page of results
        groups = paginator.page(paginator.num_pages)

    return render(request, 'students/groups_list.html',
                  {'groups': groups})

def groups_add(request):
    # was form posted?
    if request.method == "POST":
        # was form add button clicked?
        if request.POST.get('add_button') is not None:
            # errors collection
            errors = {}

            # data for group object
            data = {'notes': request.POST.get('notes')}

            title = request.POST.get('title', '').strip()
            if not title:
                errors['title'] = u"Назва є обов'язковою"
            else:
                data['title'] = title

            leader = request.POST.get('leader', '').strip()
            if leader == "":
                data['leader'] = None
            else:
                students = Student.objects.filter(pk=leader)
                if len(students) != 1:
                    errors['leader'] = u"Оберіть коректного старосту"
                else:
                    data['leader'] = students[0]

            # save student
            if not errors:
                group = Group(**data)
                group.save()

                # redirect to students list
                return HttpResponseRedirect(
                    u'%s?status_message=Групу успішно додано!' %
                    reverse('groups'))
            else:
                # render form with errors and previous user input
                return render(request, 'students/groups_add.html',
                    {'students': Student.objects.all().order_by('last_name'),
                     'errors': errors})
        elif request.POST.get('cancel_button') is not None:
            # redirect to group page on cancel button
            return HttpResponseRedirect(
                u'%s?status_message=Додавання групи скасовано!' %
                reverse('groups'))
    else:
        # initial form render
        return render(request, 'students/groups_add.html',
                      {'students': Student.objects.all().order_by('last_name')})

class GroupUpdateForm(ModelForm):
    class Meta:
        model = Group
        #fields = "__all__"
        fields = ['title', 'leader', 'notes']

    def __init__(self, *args, **kwargs):
        super(GroupUpdateForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)

        # set form tag attributes
        self.helper.form_action = reverse('groups_edit',
            kwargs={'pk': kwargs['instance'].id})
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'

        # set form field properties
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'

        # add buttons
        self.helper.layout[-1] = FormActions(
            Submit('add_button', u'Зберегти', css_class="btn btn-primary"),
            Submit('cancel_button', u'Скасувати', css_class="btn btn-link"),
        )

class GroupUpdateView(UpdateView):
    model = Group
    template_name = 'students/groups_edit.html'
    form_class = GroupUpdateForm

    def get_success_url(self):
        return u'%s?status_message=Групу успішно збережено!' \
            % reverse('groups')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(
                u'%s?status_message=Редагування групи відмінено!' %
                reverse('groups'))
        else:
            return super(GroupUpdateView, self).post(request, *args, **kwargs)

class GroupDeleteView(DeleteView):
    model = Group
    template_name = 'students/groups_confirm_delete.html'

    def get_success_url(self):
        return u'%s?status_message=Групу успішно видалено!' \
            % reverse('groups')