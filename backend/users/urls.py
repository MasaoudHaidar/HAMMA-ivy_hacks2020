from django.urls import include, path
from . import views
urlpatterns = [
    path('signup/', views.signup , name='signup'),
#    path('signup/professor',  , name='signup_professor'),
#    path('signup/company',  , name='signup_company'),
#    path('signup/student',  , name='signup_student'),
    path('login/', views.login  , name='login'),
#    path('login/professor',  , name='login_professor'),
#    path('login/company',  , name='login_company'),
 #   path('login/student',  , name='login_student'),
]