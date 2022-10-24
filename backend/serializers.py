from rest_framework import serializers
from .models import Employee, Restaurant, Vote


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['user', 'department']

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['user'] = instance.user.username
        return ret


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['name', 'menu', 'publication_date']


class VoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vote
        fields = ['user', 'menu', 'vote', 'publication_date']




