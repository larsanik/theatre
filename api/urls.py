from django.urls import path
from api.views import ActorListListView, ShowListListView

urlpatterns = [
    path('actor_lists/', ActorListListView.as_view()),
    path('show_lists/', ShowListListView.as_view()),
]