from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

from .models import Company, Professor, Problem

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

def process_add_problem(request):
    # get company or create a new one
    print(request)
    company_obj, _ = Company.objects.get_or_create(full_name__iexact=request.POST['company-name'])
    p = Problem(
        title=request.POST['problem-title'],
        description=request.POST['problem-description'],
        company=company_obj,
        date_posted=timezone.now(),
        course_content={}
    )
    p.save()
    return HttpResponseRedirect(reverse('course:index'))

def index(request):
    context = {
        'problems': Problem.objects.all()
    }
    return render(request, 'course/index.html', context)
