from django.urls import path
from main import views
from main.views import UserCreateView


urlpatterns = [
    path('api/u/<str:uname>', views.main_page, name = 'linkers/' ),
    path('api/maincreate', views.create_main, name = 'feed/' ),
    path('api/register', UserCreateView.as_view(), name = 'register/' ),
]