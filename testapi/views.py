from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class HelloWorldView(APIView):
    """
    A view that returns the exam data and id type.
    """

    def get(self, request):
        return Response({"Message":"Hello World"}, status=status.HTTP_200_OK)