from django.shortcuts import render, HttpResponse
from time import gmtime, strftime

# Create your views here.
def display_time(request):
    context = {
        "time": strftime("%A %B %d, %Y - %H:%M %p", gmtime())
    }
    return render(request, "display_time.html", context)