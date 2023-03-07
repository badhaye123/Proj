from django.shortcuts import render
from django.shortcuts import redirect
from .models import Approver, Requester, User,ApprovalRequest
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ApprovalRequestForm, RequesterSignUpForm, ApproverSignUpForm
from django.http import HttpResponse

# Create your views here.


@login_required(login_url='admin-login/')
def index(request):
    return render(request, 'index.html')


class ApproverSignUpView(LoginRequiredMixin, CreateView):
    login_url = 'admin-login/'
    model = User
    form_class = ApproverSignUpForm
    template_name = 'signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'approver'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        # login(self.request, user)
        return redirect('admin_dashboard')


class RequesterSignUpView(LoginRequiredMixin,CreateView):
    login_url = 'admin-login/'
    model = User
    form_class = RequesterSignUpForm
    template_name = 'signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'requester'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        # login(self.request, user)
        return redirect('admin_dashboard')


def admin_login(request):
    template_name = 'admin_login.html'
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request,username=username,password=password)
    if user is not None:
        login(request, user)
        return redirect('index')
    else:
        messages.error(request,"Invalid credentials")
    return render(request,template_name,{})


def approver_login(request):
    template_name = 'approver_login.html'
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request,username=username,password=password)
    if user is not None:
        login(request, user)
        return redirect('display')
    else:
        messages.error(request,"Invalid credentials")
    return render(request,template_name,{})



def requester_login(request):
    template_name = 'requester_login.html'
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request,username=username,password=password)
    if user is not None:
        login(request, user)
        return redirect('create_request')
    else:
        messages.error(request,"Invalid credentials")
    return render(request,template_name,{})


@login_required(login_url='admin-login/')
def admin_dashboard(request):
    data = User.objects.all()
    for i in data:
        print(i.username)
    template_name = 'admin_dashboard.html'
    context = {'data':data}
    return render(request, template_name, context)

def admin_logout(request):
    logout(request)
    return redirect('admin_login')


def requester_logout(request):
    logout(request)
    return redirect('requester_login')


def approver_logout(request):
    logout(request)
    return redirect('approver_login')



@login_required(login_url='requester-login/')
def create_request(request):
    form = ApprovalRequestForm()
    if request.method =='POST':
        form = ApprovalRequestForm(request.POST)
        if form.is_valid():
            request_object = form.save(commit=False)
            requester = Requester.objects.get(user = request.user)
            request_object.requester =requester
            request_object.save()
            return redirect('requester_dashboard')
    template_name = 'create_request.html'
    context = {'form':form}
    return render(request, template_name, context)


@login_required(login_url='approver-login/')
def display(request):
    approver = Approver.objects.get(user=request.user)
    approval_requests = ApprovalRequest.objects.filter(assigned_to=approver)
    context = {'approval_requests':approval_requests}
    template_name = 'approve_request.html'
    return render(request, template_name, context)

@login_required(login_url='approver-login/')
def approve_request(request,id):
    try:
        approval_request=ApprovalRequest.objects.get(id=id)
        approval_request.status=True
        approval_request.save()
        return redirect('display')
    except ApprovalRequest.DoesNotExist:
        return HttpResponse('Does not exist')

@login_required(login_url='requester-login/')
def requester_dashboard(request):
    user = Requester.objects.get(user=request.user)
    approval_request = ApprovalRequest.objects.filter(requester=user)
    context = {'approval_request':approval_request}
    template_name = 'requester_dashboard.html'
    return render(request, template_name, context)

