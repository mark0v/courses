from restapi.models import CourceResource, CategoryResource
from tastypie.api import Api
from django.urls import path, include

api = Api(api_name='v1')
api.register(CourceResource())
api.register(CategoryResource())

# For POST, DELETE add header
# Key: Authorization
# Value: ApiKey alex:170976

urlpatterns = [
    path('', include(api.urls), name='index')
]
