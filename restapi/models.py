from tastypie.resources import ModelResource
from shop.models import Category, Course
from tastypie.authorization import Authorization
from .authentication import CustomAuthentication


class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'categories'
        allowed_methods = ['get']


class CourceResource(ModelResource):
    class Meta:
        queryset = Course.objects.all()
        resource_name = 'courses'
        allowed_methods = ['get', 'post', 'delete']
        authentication = CustomAuthentication()
        authorization = Authorization()

    def hydrate(self, bundle):
        bundle.obj.cetegory_id = bundle.data['cetegory_id']
        return bundle

    def dehydrate(self, bundle):
        bundle.data['cetegory_id'] = bundle.obj.cetegory
        return bundle

    def dehydrate_title(self, bundle):
        return bundle.data['title'].upper()
