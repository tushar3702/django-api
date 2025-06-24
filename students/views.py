from django.shortcuts import render
from django.http import HttpResponse

def students(request):
    students = [
        {'id': 1, 'name': 'Tushar', 'age': 24}
    ]
    return HttpResponse(students)
