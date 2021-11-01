from rest_framework import serializers
from .models import Projectfolio,blog

# Projectfolio models

class project_serial(serializers.ModelSerializer):
    
    class Meta:
        model = Projectfolio
        fields = ['id','project_name','project_description','project_link','project_image']

class blog_serial(serializers.ModelSerializer):
    
    user = serializers.ReadOnlyField(source='user.user.username')
    
    class Meta:
        model = blog
        fields = ['id','user','title','post','date_added']