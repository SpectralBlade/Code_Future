from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Advertisements14
from .forms import Advertisements14Form

# Create your views here.
def index(request):
    advertisements = Advertisements14.objects.all()
    context = {'advertisements': advertisements}
    return render(request, 'index.html', context)

def top_sellers(request):
    return render(request, 'top-sellers.html')

def login(request):
    return render(request, 'login.html')

def profile(request):
    return render(request, 'profile.html')

def register(request):
    return render(request, 'register.html')

def advertisement(request):
    return render(request, 'advertisement.html')

def advertisement_post(request):
    if request.method == "POST":
        form = Advertisements14Form(request.POST, request.FILES)
        if form.is_valid():
            new_advertisement = form.save(commit=False)
            new_advertisement.user = request.user
            new_advertisement.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = Advertisements14Form()
    context = {'form': form}
    return render(request, 'advertisement-post.html', context)


