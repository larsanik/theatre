from rest_framework import serializers

from plays.models import Actor

class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'name', 'birthday']
