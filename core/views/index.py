from django.shortcuts import render
from core.models import Password

def index(request):
    passwords = Password.objects.all()

    return render(request, 'core/index.jinja', context={
        'passwords': passwords,
    })