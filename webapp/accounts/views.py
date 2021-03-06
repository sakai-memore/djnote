from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate


class FView(FormView):
    form_class = UserCreationForm
    template_name = 'registration/create.html'
    template_name_comfirm = 'registration/create_confirm.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        print(self.request.POST['next'])
        if self.request.POST['next'] == 'back':
            return render(self.request, template_name, {'form': form})
        elif self.request.POST['next'] == 'confirm':
            return render(self.request, template_name_confirm, {'form': form})
        elif self.request.POST['next'] == 'regist':
            form.save()
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
            )
            login(self.request, user)
            return super().form_valid(form)
        else:
            return redirect(reverse_lazy('home'))

create = FView.as_view()
