import requests
import random
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, filters
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import MultiPartParser
from testapi.models import User, Movie, UserRatings
from testapi.serializers import MovieRatingsSerializer, MovieSerializer

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


class MovieSearchView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']


class ThirdPartyApiView(APIView):

    def get(self, request):
        resp = requests.get("https://jsonblob.com/api/24ce4f7a-ad79-11ea-95e6-5df0b694a869")
        if resp.status_code == 200:
            return Response({"Data":resp.json()}, status=status.HTTP_200_OK)
        else:
            return Response({"Data":''}, status=status.HTTP_200_OK)


class AddMovieView(CreateAPIView):
    serializer_class = MovieSerializer
    parser_classes = [MultiPartParser]
    http_method_names = ["post"]

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message":"Success"}, status=status.HTTP_200_OK)
        else:
            return Response({"Message":"Failed"}, status=status.HTTP_200_OK)
