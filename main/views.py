from rest_framework import generics
from django.contrib.auth.models import User
from .models import Mainfolio
from .serializers import main_serial,UserSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework	import status
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import get_user_model 
from rest_framework.parsers import JSONParser
from rest_framework import permissions

@api_view(['get'])
def main_page(request,uname):
    if	request.method	==	'GET':
        permission_classes = (AllowAny,)
        name =  get_object_or_404(User,username=uname)
        find = get_object_or_404(Mainfolio,user=name)
        serializer_class = main_serial(find)
        return Response(serializer_class.data)

@api_view(['post'])        
def  create_main(request):      
    if request.method == 'POST':
        authentication_classes = (TokenAuthentication,)
        permission_classes = (IsAuthenticated,)
        name = request.user
        image = request.data.get("image")
        text = request.data.get("text")
        fb = request.data.get("fb")
        lk = request.data.get("lk")
        tw = request.data.get("tw")
        dr = request.data.get("dr")
        re = request.data.get("re")
        permission_classes = (IsAuthenticated,)
        find = Mainfolio.objects.create(user=name,welcome_image=image,welcome_text=text,facebook=fb,linkliden=lk,twitter=tw,dribble=dr,resume=re)
        serializer_class = main_serial(find)
        return Response(serializer_class.data)
    
    else:
        return Response(status=status.HTTP_401_BAD_REQUEST)

class UserCreateView(generics.CreateAPIView):
    model = get_user_model()
    parser_classes = [JSONParser]
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer
