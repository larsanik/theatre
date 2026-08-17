from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
from rest_framework import generics

from api.serializers import ActorListSerializer, ShowListSerializer
from plays.models import Actor, Show

from rest_framework import permissions
from api.permissions import IsOwner


# Create your views here.
class ActorListListView(generics.ListAPIView):
    serializer_class = ActorListSerializer
    queryset = Actor.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsOwner]

class ShowListListView(generics.ListAPIView):
    serializer_class = ShowListSerializer
    queryset = Show.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsOwner]
