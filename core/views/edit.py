from django.shortcuts import render, get_object_or_404, redirect
from core.models import Password
from core.forms import Creation

def edit(request, pw_slug):
    password = get_object_or_404(Password, slug=pw_slug)
    if request.method == 'POST':
        form = Creation(request.POST, instance=password)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = Creation(instance=password)

    return render(request, 'core/edit.jinja', context={
        'form':form,
    })