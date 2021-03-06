from django.urls import path

from . import views

app_name = 'course'
urlpatterns = [
    # e.g., /courses
    path('', views.index, name='index'),
    # e.g., /courses/1
    path('<int:course_id>', views.detail, name='detail'),
    # e.g., /courses/add_problem/
    path('add_problem/', views.add_problem, name='add_problem'),
    path('process_add_comment/<int:problem_id>', views.process_add_comment, name='process_add_comment'),
    path('process_add_solution/<int:problem_id>', views.process_add_solution, name='process_add_solution'),
]
