from django.urls import path
from .views import *

urlpatterns = [
    path('register/',Registeration_view.as_view(), name = 'Register'),
    path('login/', Login_View.as_view(), name = 'Login'),
    path('users/', UserView.as_view(), name = 'users'),
    path('attendance/<str:action>/', Attendance_View.as_view(), name = 'Attendance'),

]