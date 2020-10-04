from django.urls import include, path
from . import views
urlpatterns = [
    path('signup/',  , name='signup'),
    path('signup/professor',  , name='signup_professor'),
    path('signup/company',  , name='signup_company'),
    path('signup/student',  , name='signup_student'),
]