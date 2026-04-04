from django.db import models
from django.contrib.admin import display
from django.urls import reverse
from django.db.models import functions


# Create your models here.
class Play(models.Model):
    title = models.CharField(max_length=255)
    annotation =models.TextField()


class Actor(models.Model):
    name = models.CharField(max_length=255)
    birthday = models.DateField(null=True)

class ShowManager(models.Manager):
    def active(self):
       return self.get_queryset().filter(starts_at__gt=functions.Now())


class Show(models.Model):
    starts_at = models.DateTimeField()
    play = models.ForeignKey(Play, on_delete=models.CASCADE)
    actor = models.ManyToManyField(Actor)
    objects = ShowManager()

    @display
    def play_name(self):
        return self.play.title

    def get_absolute_url(self):
        return reverse('show_detail', kwargs={'pk': self.pk})
