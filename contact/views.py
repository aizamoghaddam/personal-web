from django.shortcuts import render, redirect
from.forms import *
from .models import *


def contact(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Comment.objects.create(name=cd['name'], email=cd['email'], comment=cd['comment'])
            return redirect('home')
    else:
        form = CommentForm()
    return render(request, 'contact.html', {'form': form})


