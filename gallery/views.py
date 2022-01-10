from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.


def gallery_index(request):
    return render(request, 'gallery.html')


def christmas(request):
    return render(request, 'christmas.html')
