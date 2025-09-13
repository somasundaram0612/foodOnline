from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # return HttpResponse('Hello Mugilaa!!') # after first commit
    return render(request, 'home.html')