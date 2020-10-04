from django.urls import include, path
from . import views

app_name = 'users'
urlpatterns = [
    path('signup/', views.signup , name='signup'),
    path('login/', views.login  , name='login'),
]
