from django.db import models
from django.contrib.admin import display
from django.urls import reverse
from django.db.models import functions
from users.models import User


# Create your models here.
class Play(models.Model):
    title = models.CharField(max_length=255)
    annotation =models.TextField()
    def __str__(self):
        return self.title

class Actor(models.Model):
    name = models.CharField(max_length=255)
    birthday = models.DateField(null=True)
    def __str__(self):
        return self.name

class ShowManager(models.Manager):
    def active(self):
       return self.get_queryset().filter(starts_at__gt=functions.Now())


class Show(models.Model):
    starts_at = models.DateTimeField()
    play = models.ForeignKey(Play, on_delete=models.CASCADE)
    actor = models.ManyToManyField(Actor)
    objects = ShowManager()

    def __str__(self):
        # Выведет, например: "Наладка на Острогожской — 2027-08-17 17:00:00"
        return self.play.title

    @display
    def play_name(self):
        return self.play.title

    def get_absolute_url(self):
        return reverse('show_detail', kwargs={'pk': self.pk})


class Booking(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    place = models.IntegerField()

    class Meta:
        # Этот констрейнт позвояет выставить требование уникальности на пару (представление, место)
        # Это позволит избежать двух бронирований на одно место
        unique_together = ('show', 'place')
