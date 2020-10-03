from django.urls import path

from . import views

app_name = 'course'
urlpatterns = [
    path('<int:course_id>/<slug:slug>', views.detail),
    path('add_problem/', views.add_problem),
]
