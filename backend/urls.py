from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('employee/', views.EmployeeList.as_view()),
    path('employee/<int:pk>/', views.EmployeeDetail.as_view()),
    path('restaurant/', views.RestaurantList.as_view()),
    path('restaurant/<int:pk>/', views.RestaurantDetail.as_view()),
    path('restaurant/<int:restaurant_pk>/<int:user_pk>/vote/', views.RestaurantVoteView.as_view()),
    path('menu/', views.MenuView.as_view()),
    path('results/', views.ResultsView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

#   authentication
#   getting current day menu

