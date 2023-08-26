from django.contrib import messages
from django.shortcuts import render
from . import models


# Create your views here.
from .forms import RegisterForm


def register_user(request):
    if request.method == 'GET':
        form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Profile details updated.')

    context = {
        'form': form,
    }

    return render(request, 'register.html', context=context)


def users_list(request):
    deps = models.Node.objects.filter(
        types=models.Node.TypeList.DEPARTMENT
    )

    users = None
    if request.user.is_superuser:
        users = models.UserPosition.objects.all()

    context = {
        'deps': deps,
        'users': users,
    }

    return render(request, 'user.html', context=context)
