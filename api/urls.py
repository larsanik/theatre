from django.urls import path
from api.views import ActorListListView

urlpatterns = [
    path('actor_lists/', ActorListListView.as_view()),
]