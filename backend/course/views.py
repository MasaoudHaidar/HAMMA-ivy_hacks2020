from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

from .models import *
from users.models import Company, Student, Professor

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
def detail(request, course_id):
    p = get_object_or_404(Problem, pk=course_id)
    # get all discussions for the problem
    discussions = Discussion.objects.filter(problem__pk=course_id)
    # get all solutions for the problem
    solutions = Solution.objects.filter(problem__pk=course_id)
    context = {
        'problem': p,
        'discussions': discussions,
        'solutions': solutions,
    }
    if request.user.is_authenticated:
        user = request.user
        if Company.objects.filter(user=request.user).exists():
            context["is_company"] = True
        if Student.objects.filter(user=request.user).exists():
            context["is_student"] = True
        if Professor.objects.filter(user=request.user).exists():
            context["is_professor"] = True
    return render(request, 'course/problem_page.html', context)

@login_required
def add_problem(request):
    company_set = Company.objects.filter(user=request.user)
    if company_set.exists():
        if request.method == 'POST':
            p = Problem(
                title=request.POST['problem-title'],
                description=request.POST['problem-description'],
                company=company_set.first(),
                date_posted=timezone.now(),
            )
            p.save()
            return HttpResponseRedirect(reverse('course:index'))
        else:
            return render(request, 'course/add_problem.html')
    else:
        return HttpResponseRedirect(reverse('course:index'))

def process_add_comment(request, problem_id):
    p = get_object_or_404(Problem, pk=problem_id)
    student_obj, student_created = Student.objects.get_or_create(full_name__iexact='Student') # TODO: link login page with student full_name
    if student_created:
        student_obj.full_name = 'Student'
        student_obj.save()
    d = Discussion(
        problem=p,
        student=student_obj,
        comment=request.POST['comment']
    )
    d.save()
    return HttpResponseRedirect(reverse('course:detail', args=(problem_id, )))

def process_add_solution(request, problem_id):
    p = get_object_or_404(Problem, pk=problem_id)
    professor_obj, professor_created = Professor.objects.get_or_create(full_name__iexact='Professor') # TODO: link login page with professor full_name
    if professor_created:
        professor_obj.full_name = 'Professor'
        professor_obj.save()
    s = Solution(
        problem=p,
        date_solved=timezone.now(),
        professor=professor_obj,
        video_url=request.POST['solution-video'],
        solution_text=request.POST['solution-text'],
    )
    s.save()
    return HttpResponseRedirect(reverse('course:detail', args=(problem_id, )))

def index(request):
    context = {
        'problems': Problem.objects.all()

    }
    return render(request, 'course/index.html', context)
