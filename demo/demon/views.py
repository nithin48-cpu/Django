from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm


def index(request):
    # return HttpResponse("welcome")
    # if not find html file write 'dir_name' in DIRS in settings file
    return render(request, 'index.html')


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #return redirect('result.html')
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

# def register(request):
#     return render(request, 'register.html')


def result(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        mail = request.POST['mail']
        return render(request, 'registration/result.html', {'fname': fname, 'lname': lname, 'mail': mail})
