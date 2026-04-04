from django.views.generic import ListView

from plays.models import Show


# Create your views here.
class HomepageView(ListView):
    template_name = 'homepage.html'
    model = Show
    def get_queryset(self):
        return Show.objects.active()