from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class LandingPage(TemplateView):
    template_name="webpage/landingpage.html"