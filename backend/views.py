import json
import datetime

from django.http import HttpResponse
from .models import Employee, Restaurant, Vote
from .serializers import RestaurantSerializer, VoteSerializer, EmployeeSerializer
from rest_framework import generics


class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class RestaurantList(generics.ListCreateAPIView):
    serializer_class = RestaurantSerializer
    #   queryset = Restaurant.objects.all()

    def get_queryset(self):
        return Restaurant.objects.filter(publication_date=datetime.date.today())


class RestaurantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class RestaurantVoteView(generics.CreateAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer


class MenuView(generics.ListAPIView):
    serializer_class = VoteSerializer

    def get(self, request, *args, **kwargs):
        menu = Restaurant.objects.filter().values_list('name', 'menu')
        mimetype = 'application/json'
        return HttpResponse(json.dumps({'menu': str(menu)}), mimetype)
#   publication_date=datetime.date.today() (add this line later in filter)


class ResultsView(generics.ListAPIView):
    serializer_class = VoteSerializer

    def get(self, request, *args, **kwargs):
        vote_count = Vote.objects.filter().values_list('menu__name', 'vote')
        mimetype = 'application/json'
        return HttpResponse(json.dumps({'Results': str(vote_count)}), mimetype)
#   publication_date=datetime.date.today() (add this line later in filter)
