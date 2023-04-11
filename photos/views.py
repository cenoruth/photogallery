from django.shortcuts import render, redirect
from .models import Category, Photo
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm

# Create your views here.

def loginUser(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('gallery')

    return render(request, 'photos/login_register.html', {'page': page})

def logoutUser(request):
    logout(request)
    return redirect('gallery')

def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            user = authenticate(request, username=user.username, password=request.POST['password1'])

            if user is not None:
                login(request, user)
                return redirect('gallery')

    context = {'form': form, 'page': page}
    return render(request, 'photos/login_register.html', context)


def gallery(request):
    category = request.GET.get('category')
    page = request.GET.get('page', 1)
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)

    #paginator = Paginator(photos, 10)
    #try:
    #    photos_page = paginator.page(page)
    #except PageNotAnInteger:
    #    photos_page = paginator.page(1)
    #except EmptyPage:
    #    photos_page = paginator.page(paginator.num_pages)

    categories = Category.objects.all()
    context = {'categories': categories, 'photos': photos}
    return render(request, 'photos/gallery.html', context)

def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'photos/photo.html', {'photo': photo})

def addPhoto(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')

        if data['category'] != 'none': 
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = None

        for image in images:
            photo = Photo.objects.create(
                submitter=data['submitter'],
                category=category,
                image=image,
            )

        return redirect('gallery')

    context = {'categories': categories}
    return render(request, 'photos/add.html', context)