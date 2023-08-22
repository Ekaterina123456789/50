from django.shortcuts import render, redirect, get_object_or_404
from .models import Catalog
from .forms import WorkForm


def portfolio(request):
    works = Catalog.objects.all()
    return render(request, 'userpage/works.html', {'works': works})


def add_work(request):
    if request.method == 'POST':
        form = WorkForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('works')
    else:
        form = WorkForm()
    return render(request, 'userpage/add_work.html', {'form': form})

