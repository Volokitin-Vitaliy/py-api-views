from django.urls import path, include
from rest_framework import routers

from cinema.views import GenreListCreateAPIView, GenreDetailAPIView, ActorListCreateAPIView, \
    ActorDetailAPIView, CinemaHallViewSet, MovieViewSet

router = routers.DefaultRouter()
router.register("cinema-halls", CinemaHallViewSet, basename="cinemahall")
router.register("movies", MovieViewSet, basename="movie")

urlpatterns = [
    path("genre/", GenreListCreateAPIView.as_view(), name="genre-list-create"),
    path("genre/<int:pk>/", GenreDetailAPIView.as_view(), name="genre-detail"),
    path("actor/", ActorListCreateAPIView.as_view(), name="actor-list-create"),
    path("actor/<int:pk>/", ActorDetailAPIView.as_view(), name="actor-detail"),
    path("", include(router.urls))

]

app_name = "cinema"
