from django.shortcuts import render
from django.http import HttpResponseNotFound

# Create your views here.
def detail(request, course_id, slug):
    return HttpResponseNotFound('<h1>Page not created yet</h1>')

def add_problem(request):
    return render(request, 'course/add_problem.html')
    # return HttpResponseNotFound('<h1>Page not created yet</h1>')
