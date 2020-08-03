from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from testapi.models import User, Movie, UserRatings
from testapi.serializers import MovieRatingsSerializer

class HelloWorldView(APIView):

    def get(self, request):
        return Response({"Message":"Hello World"}, status=status.HTTP_200_OK)


class ComputationTestView(APIView):

    def get(self, request):
        count = 0
        n1, n2 = 0, 1
        res = []
        while count < 1000:
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            count += 1
            
        return Response({"Message":"Done"}, status=status.HTTP_200_OK)


class MovieListView(APIView):

    def get(self, request, format=None):
        movies = [movie.title for movie in Movie.objects.all()]
        return Response({"Movies":movies}, status=status.HTTP_200_OK)


class MovieRatingsView(generics.RetrieveAPIView):
    serializer_class = MovieRatingsSerializer
    queryset = Movie.objects.all()
    lookup_field = "id"

    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            self.get_object(), context={"request": request}
        )
        return Response({"Movie":serializer.data}, status=status.HTTP_200_OK)

