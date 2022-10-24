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


class ResultsView(generics.ListAPIView):
    serializer_class = VoteSerializer

    def get(self, request, *args, **kwargs):
        vote_count = Vote.objects.filter(publication_date=datetime.date.today()).values_list(
            'user__username', 'menu__name', 'vote', 'publication_date')

        return HttpResponse(vote_count)








 #   ('Restaurant 1',)('Restaurant 2',)('Restaurant 4',)('Restaurant 5',)('Restaurant 6',)
#   (1,)(1,)(1,)(1,)(1,)(1,)(1,)(1,)(1,)(1,)(2,)(1,)
        # mimetype = 'application/json'
        #return HttpResponse(json.dumps({'Restaurants': str(restaurant)}), mimetype)

