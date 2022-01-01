from django.shortcuts import render
from django.views import View

class CView(View):
    def get(self, request, *arg, **kwargs):
        context = {
            "title": "Django"
        }
        return render(request, '_hello.hbs', context)
        
hello = CView.as_view()
