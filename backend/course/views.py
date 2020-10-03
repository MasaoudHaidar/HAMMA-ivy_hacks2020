from django.shortcuts import render
from django.http import HttpResponseNotFound

problems = [
    {
        'title': '1',
        'description': 'blah',
    },
    {
        'title': '2',
        'description': 'blah blah',
    },
]

# Create your views here.
def detail(request, course_id, slug):
    return HttpResponseNotFound('<h1>Page not created yet</h1>')

def add_problem(request):
    return render(request, 'course/add_problem.html')
    # return HttpResponseNotFound('<h1>Page not created yet</h1>')

def index(request):
    context = {
        'problems': problems
    }
    return render(request, 'course/index.html', context)
