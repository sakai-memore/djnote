from django.shortcuts import render

# Create your views here.
def hello(request):
    context = {
        "title": "Django"
    }
    return render(request, '_hello.hbs', context)
