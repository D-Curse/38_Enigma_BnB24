from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .forms import HRForm
from .models import HR

# Create your views here.

def home(request):
    return render(request, 'home.html')

def auth_view(request):
    return render(request, 'auth/auth_view.html')

def user_signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        errors = {}
        
        if User.objects.filter(username=username).exists():
            errors['existing_user'] = True
        if confirm_password != password:
            errors['errors_password'] = True
        try:
            validate_password(password)
        except ValidationError as error:
            errors['error_pass_validation'] = error
            
        if errors:
            print(errors)
            errors.update({'error': True, 'username': username, 'password': password})
            return render(request, "auth/auth_view.html", {'errors': errors})
        else:
            myuser = User.objects.create_user(username=username, password=password)
            myuser.save()
            return render(request, "core/user_form.html",)
    return render(request, 'auth/auth_view.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password'] 
        user = authenticate(username=username, password=password)

        
        if user is not None:
            login(request, user)
            return redirect('profile_form')
        else:
            return render(request, "auth/auth_view.html", {'error_invalid':True})
    return render(request, 'profile_form.html')

def hr_login(request):
    if request.method == 'POST':
        hr_name = request.POST.get('name')
        hr_uuid = request.POST.get('uuid')

        try:
            hr = HR.objects.get(name=hr_name, uuid=hr_uuid)
            return redirect('dashboard') 
        except HR.DoesNotExist:
            return render(request, 'auth/auth_view.html', {'error_invalid': True})

    return render(request, 'auth/auth_view.html.html')

def admin_page(request):
    if request.method == 'POST':
        form = HRForm(request.POST)
        if form.is_valid():
            hr = form.save()
            return render(request, 'admin/admin_page.html', {'hr': hr})
    else:
        form = HRForm()
    
    return render(request, 'admin/admin_page.html', {'form': form})

def get_hr_uuid(request):
    if request.method == 'POST':
        hr_name = request.POST.get('name')
        try:
            hr = HR.objects.get(name=hr_name)
            return render(request, 'admin/admin_page.html', {'hr': hr})
        except HR.DoesNotExist:
            return render(request, 'admin/admin_page.html', {'error_not_found': True})

    return render(request, 'admin/admin_page.html')