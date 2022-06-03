from django.shortcuts import render
from .models import tweet
from django.views.generic import ListView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class TweetListView(LoginRequiredMixin,ListView):
    model = tweet
    template_name = 'feed/home.html'
    ordering = ['-datetime']

class TweetCreateView(LoginRequiredMixin,CreateView):
    model = tweet
    fields =['text']
    template_name = 'feed/create.html'
    success_url = '/'

    def form_valid(self,form):
        form.instance.uname = self.request.user
        return super().form_valid(form)


