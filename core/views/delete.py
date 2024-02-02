from django.shortcuts import get_object_or_404, redirect
from core.models import Password

def delete(request, pw_slug):
    password = get_object_or_404(Password, slug=pw_slug)
    if password:
        password.delete()
        return redirect('index')