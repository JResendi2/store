from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomLoginForm
from django.contrib.auth.models import User, Permission
from .forms import CustomUserForm
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.template.loader import render_to_string

def login_in(request):
    if request.method == 'POST':
        
        form = CustomLoginForm(request, data=request.POST)
   
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('product_index') # Cambia esto a tu URL de éxito
            else:
                form.add_error(None, 'Invalid username or password') # Manejo de error de autenticación fallida
    else:
        form = CustomLoginForm()
    return render(request, 'login-admin/login.html', {'form': form})


def login_up(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
             
            user = User.objects.get(username=username)
            permission = Permission.objects.get(codename='change_products')
            user.user_permissions.add(permission)
            
            user_authenticate = authenticate(username=username, password=password)
            if user_authenticate is not None:
                login(request, user_authenticate)
                return redirect('product_index') # Cambia esto a tu URL de éxito
    else:
        form = CustomUserForm()
    return render(request, 'login-admin/register.html', {"form": form})


def loggedin_user(request):
    if request.user.is_authenticated:
        datos = {
            'body': f'Hola, {request.user.username}. Estás autenticado.',
            'authenticated': True
        }
    else:
        form = CustomLoginForm()
        template_login = render_to_string('login-client/login.html', {"form": form})
    
        datos = {
            'body': template_login,
            'authenticated': False
        }
    return JsonResponse(datos)


def login_in_client(request):
    if request.method == 'POST':
        datos = {}
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                datos = {
                    'body': "Inicio de sesión correcto",
                    'session': True
                }
            else:
                template_login = render_to_string('login-client/login.html', {"form": form})
                
                datos = {
                    'body': template_login,
                    'session': True
                }
        else:
            template_login = render_to_string('login-client/login.html', {"form": form})
                
            datos = {
                'body': template_login,
                'session': False
            }
    return JsonResponse(datos)

def login_up_client(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        
        if form.is_valid():
            form.save()
            form = CustomLoginForm()
            template_login = render_to_string('login-client/login.html', {"form": form})
        
            datos = {
                'body': template_login,
                'session': False
            }
        template_register = render_to_string('login-client/register.html', {"form": form})
        
        datos = {
            'body': template_register,
            'session': False
        }
    else:
        form = CustomUserForm()
        template_register = render_to_string('login-client/register.html', {"form": form})
        
        datos = {
            'body': template_register,
            'session': False
        }
    return JsonResponse(datos)