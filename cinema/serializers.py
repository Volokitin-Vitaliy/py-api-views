from rest_framework import serializers
from rest_framework import serializers
from .models import Actor, Genre, CinemaHall, Movie


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'first_name', 'last_name']


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']


class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ['id', 'name', 'rows', 'seats_in_row']


class MovieSerializer(serializers.Serializer):
    actors = serializers.PrimaryKeyRelatedField(queryset=Actor.objects.all(), many=True)
    gernes = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all(), many=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'duration', 'actors', 'genres']
