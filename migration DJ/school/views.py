from django.http import HttpResponse
from django.views.generic import ListView
from django.shortcuts import render

from .models import Student, Teacher


def students_list(request):
    template = 'school/students_list.html'
    students = Student.objects.all()
    context = {'object_list': students}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = 'group'

    return render(request, template, context)


def theacher(request):
    students = Student.objects.all()
    list_data = []
    for element in students:
        all_teacher = element.teacher.all()
        list_techer= []
        for teacher in all_teacher:
            list_techer.append(teacher.subject)
        print(f'Имя ученика: {element}\nУчителя:{list_techer}')
        list_data.append(element.name)




    return HttpResponse(list_data)

