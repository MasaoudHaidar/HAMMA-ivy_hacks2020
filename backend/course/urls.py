from django.urls import path

from . import views

app_name = 'course'
urlpatterns = [
    # e.g., /courses/1/how-to/
    path('<int:course_id>/<slug:slug>', views.detail, name='detail'),
    # e.g., /courses/add_problem/
    path('add_problem/', views.add_problem, name='add_problem'),
]
