from django.shortcuts import render

from django.views import generic

from plays.models import Show


# Create your views here.
class ShowDetailView(generic.DetailView):
    model = Show
