from django.shortcuts import render

# Create your views here.
def root(request):
    context = {
        "title": "Django"
    }
    return render(request, 'users/_users.hbs', context)
