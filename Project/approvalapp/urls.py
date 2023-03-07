from django.urls import path
from .views import *

urlpatterns = [
    path('index/', index, name='index'),
    path('requester/', RequesterSignUpView.as_view(), name='requester_signup'),
    path('approver/', ApproverSignUpView.as_view(), name='approver_signup'),
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('admin-login/', admin_login, name='admin_login'),
    path('admin-logout/', admin_logout, name='admin_logout'),
    path('requester-login/', requester_login, name='requester_login'),
    path('requester-logout/', requester_logout, name='requester_logout'),
    path('approver-login/', requester_login, name='approver_login'),
    path('approver-logout/', requester_logout, name='approver_logout'),
    path('requester-dashboard/', requester_dashboard, name='requester_dashboard'),
    path('display/', display, name='display'),
    path('create-request/', create_request, name='create_request'),
    path('approve-request/<int:id>', approve_request, name='approve_request')
]
