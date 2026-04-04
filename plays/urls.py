from django.urls import path

from plays.views import ShowDetailView

urlpatterns = [
    path('<int:pk>', ShowDetailView.as_view(), name='show_detail'),
]