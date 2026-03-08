from django.shortcuts import render,redirect,get_object_or_404
from .models import Note
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .forms import SignupForm


def signup_view(request):

    form = SignupForm()

    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return redirect("login")

    return render(request,"notes/signup.html",{"form":form})


def login_view(request):

    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request,username=username,password=password)

        if user:
            login(request,user)
            return redirect("dashboard")

    return render(request,"notes/login.html")


@login_required
def dashboard(request):

    query = request.GET.get("q")

    notes = Note.objects.filter(user=request.user)

    if query:
        notes = notes.filter(title__icontains=query)

    return render(request,"notes/dashboard.html",{"notes":notes})


@login_required
def add_note(request):

    if request.method == "POST":

        title = request.POST["title"]
        content = request.POST["content"]

        Note.objects.create(
            user=request.user,
            title=title,
            content=content
        )

    return redirect("dashboard")


@login_required
def edit_note(request,id):

    note = get_object_or_404(Note,id=id,user=request.user)

    if request.method == "POST":

        note.title = request.POST["title"]
        note.content = request.POST["content"]

        note.save()

        return redirect("dashboard")

    return render(request,"notes/edit.html",{"note":note})


@login_required
def delete_note(request,id):

    note = get_object_or_404(Note,id=id,user=request.user)
    note.delete()

    return redirect("dashboard")


def logout_view(request):
    logout(request)
    return redirect("login")