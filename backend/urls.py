from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework_simplejwt import views as jwt_views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="Social Network, TestTask, Oleksandr Nykolyak",
      default_version='v1',
      description="Social Network",
      terms_of_service="https://",
      contact=openapi.Contact(email="nykolyak.o@gmail.com", phone="380638878882"),
      license=openapi.License(name="Some License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('employee/', views.EmployeeList.as_view()),
    path('employee/<int:pk>/', views.EmployeeDetail.as_view()),
    path('restaurant/', views.RestaurantList.as_view()),
    path('restaurant/<int:pk>/', views.RestaurantDetail.as_view()),
    path('restaurant/<int:restaurant_pk>/<int:user_pk>/vote/', views.RestaurantVoteView.as_view()),
    path('menu/', views.MenuView.as_view()),
    path('results/', views.ResultsView.as_view()),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('playground/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
#eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY2Njk4MzA1LCJpYXQiOjE2NjY2OTgwMDUsImp0aSI6Ijg5YTAwNmFjODRmZDRmNjRhZDFhYmE3YWIyYTQ3YjEyIiwidXNlcl9pZCI6MX0.KIoaClSpLaRDO8yl_XLV0HUkYujIrX79cZCjO0U0k9A
urlpatterns = format_suffix_patterns(urlpatterns)

#   authentication
#   getting current day menu

