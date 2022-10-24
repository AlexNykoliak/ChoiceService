from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=25)

    def __str__(self):
        return self.user.username


class Restaurant(models.Model):
    name = models. CharField(max_length=25, verbose_name='restaurant_name', help_text='write the choice the name')
    menu = models.ImageField(upload_to='static/menu')
    publication_date = models.DateField(format('%Y-%m-%d'), auto_now_add=True)

    def __str__(self):
        return "{}, {}".format(self.name, self.publication_date)


class Vote(models.Model):
    user = models.ForeignKey(User, related_name='user_like', on_delete=models.CASCADE)
    menu = models.ForeignKey(Restaurant, related_name='menu_like', on_delete=models.CASCADE)
    vote = models.SmallIntegerField(default=0)
    publication_date = models.DateField(format('%Y-%m-%d'), auto_now_add=True)
