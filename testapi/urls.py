from django.urls import path
from .views import HelloWorldView, ComputationTestView, MovieListView, MovieRatingsView

urlpatterns = [
    path('helloworld/', HelloWorldView.as_view(), name="HelloWorld"),
    path('computation/', ComputationTestView.as_view(), name="computation"),
    path('movielist/', MovieListView.as_view(), name="movielist"),
    path(
        "get-movie-ratings/<int:id>/",
        MovieRatingsView.as_view(),
        name="get-movie-ratings",
    ),
]
