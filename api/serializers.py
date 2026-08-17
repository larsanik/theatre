from rest_framework import serializers

from plays.models import Actor, Show

class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'name', 'birthday']


class ShowListSerializer(serializers.ModelSerializer):
    play = serializers.StringRelatedField()
    actor = serializers.StringRelatedField(many=True)

    class Meta:
        model = Show
        fields = ['id', 'starts_at', 'play', 'actor']
