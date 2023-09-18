from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def result(request):
    n1 = int(request.POST['n1'])
    n2 = int(request.POST['n2'])
    res = n1 + n2
    return render(request, 'result.html', {'result': res})
