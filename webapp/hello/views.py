from django.shortcuts import render
from django.views import View

from django.views.generic.edit import FormView
from .forms import CForm

### view 
class CView(View): ## View Class based
    def get(self, request, *arg, **kwargs):
        TEMPLATE ='_hello.hbs'
        context = {
            "title": "Django"
        }
        return render(request, TEMPLATE, context)

hello = CView.as_view()

### form view
class FView(FormView): ## FormView Class based
    TEMPLATE = '_form.hbs'
    form_class = CForm
    template_name = (TEMPLATE)
    success_url = '/home/'

    def form_valid(self, form):
        return super().form_valid(form)

form = FView.as_view()

