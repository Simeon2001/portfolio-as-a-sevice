from django.urls import path
from project import views

urlpatterns = [
    path('api/project/<str:uname>', views.project_page, name = 'linkers/' ),
    path('api/project/<int:pk>', views.delete_it, name = 'delete/' ),
    path('api/b/<str:uname>', views.blog_page, name = 'linkers/' ),
    path('api/project', views.create_project, name = 'feed/' ),
    path('api/blog', views.create_blog, name = 'feed/' ),

]