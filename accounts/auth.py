from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_function):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('service')
        else:
            return view_function(request, *args, **kwargs)
    return wrapper_function

def admin_only(view_function):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_staff:
            return view_function(request, *args, **kwargs)
        else:
            return redirect('service')
    return wrapper_function

def user_only(view_function):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_staff:
            return redirect('admin_dashboard')
        else:
            return view_function(request, *args, **kwargs)
    return wrapper_function
