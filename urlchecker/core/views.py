from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from core.models import Url


@login_required(login_url='/accounts/login/')
def main_page(request):
    context = {'urls': Url.objects.all()}
    return render(request, 'index.html', context)
