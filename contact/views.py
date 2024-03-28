from django.shortcuts import render, redirect
from.forms import *
from .models import *
from django.contrib import messages


def contact(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Comment.objects.create(name=cd['name'], email=cd['email'], comment=cd['comment'])
            messages.success(request, 'your messages successful send! ', 'success')
            return redirect('contact')
    else:
        form = CommentForm()
    return render(request, 'contact.html', {'form': form})


