from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

#class HomePageView(TemplateView):
    #template_name = 'home.html'
def home_page_view(request):
    return HttpResponse('<h1>Hello Umed Dalbayobsan</h1>')

from django.views.generic import TemplateView
class HomePageView(TemplateView):
    template_name = 'home.html'
class AboutPageView(TemplateView):
    template_name = 'about.html'        