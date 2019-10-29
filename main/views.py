from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from . models import Website, Comment
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import UserForm, CommentForm


def homepage(request):
    return render(request = request,
                  template_name = "main/home.html",
                  context ={ 'web_view': Website.objects.all})

def details(request, pk):
    web = Website.objects.get(pk=pk)
    comments = Comment.objects.filter(post=web)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(author = form.cleaned_data["author"],
                              body = form.cleaned_data["body"],
                              post=web, )
            comment.save()
            return redirect('main:details',pk=web.pk)
            
    else:
            form = CommentForm()    
        
    return render(request,
                  "main/details.html",
                  context = {'web':web,
                             'comments':comments,
                             'form':form})



"""def details_slug(request, details_slug):
    web_view = [w.slug for w in Website.objects.all()]
    if details_slug in web_view:
        this_detail = Website.objects.get(slug = details_slug)
        return render(request,
                      "main/details.html",
                      {"web": this_detail})
    return HttpResponse(f"{details_slug} not found")"""


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New Account Created: {username}" )
            login(request, user)
            messages.info(request, f"You are now logged in as {username}" )
            return redirect("main:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg} : {form.error_messages[msg]}")


    form = UserForm
    return render(request,
                "main/register.html",
                 context = {"form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("main:homepage")


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}" )
                return redirect("main:homepage")
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")



    form = AuthenticationForm()
    return render(request,
                  "main/login.html",
                  {"form": form})




