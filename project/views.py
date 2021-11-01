from django.contrib.auth.models import User
from main.models import Mainfolio
from .models import Projectfolio,blog
from .serializers import project_serial,blog_serial
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework	import status
from rest_framework.authentication import TokenAuthentication


@api_view(['get'])
def project_page(request,uname):
    if	request.method	==	'GET':
        permission_classes = (AllowAny,)
        name =  get_object_or_404(User,username=uname)
        user = Mainfolio.objects.get(user=name)
        find = Projectfolio.objects.filter(user=user).order_by('-date_added')
        serializer_class = project_serial(find,many=True)
        return Response(serializer_class.data)

@api_view(['post'])        
def  create_project(request):      
    if request.method == 'POST':
        authentication_classes = (TokenAuthentication,)
        permission_classes = (IsAuthenticated,)
        user = request.user
        projectname = request.data.get("projectname")
        description = request.data.get("description")
        link = request.data.get("link")
        image = request.data.get("image")
        name = Mainfolio.objects.get(user=user)
        find = Projectfolio.objects.create(user=name,project_image=image,project_description=description,project_name=projectname,project_link=link)
        find.save()
        serializer_class = project_serial(find)
        return Response(serializer_class.data)
    
    else:
        return Response(status=status.HTTP_401_BAD_REQUEST)

@api_view()
def delete_it(request,pk):  
    find = Projectfolio.objects.get(id=1)
    return Response(
            {
                "status": True,
                "message": "deleted",
            }
        )

@api_view(['get'])
def blog_page(request,uname):
    if	request.method	==	'GET':
        permission_classes = (AllowAny,)
        name =  get_object_or_404(User,username=uname)
        user = Mainfolio.objects.get(user=name)
        find = blog.objects.filter(user=user).order_by('-date_added')
        serializer_class = blog_serial(find,many=True)
        return Response(serializer_class.data)

@api_view(['post'])        
def  create_blog(request):      
    if request.method == 'POST':
        authentication_classes = (TokenAuthentication,)
        permission_classes = (IsAuthenticated,)
        user = request.user
        title = request.data.get("title")
        post = request.data.get("post")
        name = Mainfolio.objects.get(user=user)
        find = blog.objects.create(user=name,title=title,post=post)
        serializer_class = blog_serial(find)
        return Response(serializer_class.data)
    
    else:
        return Response(status=status.HTTP_401_BAD_REQUEST)
