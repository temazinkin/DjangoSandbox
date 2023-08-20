from django.shortcuts import render
from . import models


# Create your views here.

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
