from django.apps import AppConfig


class ProjectConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'project'

"""
curl -i -X GET \
   -H "Vary:Accept" \
   -H "Allow:POST" \
 'http://127.0.0.1:8000/api/p/bose'
"""