from django.shortcuts import render, redirect
from core.forms import Creation
import random
import string

def add(request):
    recommended = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(25))
    if request.method == 'POST':
        form = Creation(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = Creation()

    return render(request, 'core/add.jinja', context={
        'form':form,
        'recommended':recommended,
    })