from django.shortcuts import render, redirect
from .models import Film
from .forms import FilmForm

def film_create_view(request):
    if request.method == 'POST':
        form = FilmForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('film_list')
    else:
        form = FilmForm()
    return render(request, 'films/film_create.html', {'form': form})

def film_list_view(request):
    films = Film.objects.all()
    return render(request, 'films/film_list.html', {'films': films})

