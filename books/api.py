from books.models import Author
from django.contrib.auth.models import User
from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS


class AuthorResource(ModelResource):
    class Meta:
        queryset = Author.objects.all()
        resource_name = 'author'
        authorization = Authorization()
        filtering = {
            'first_name': ALL_WITH_RELATIONS,
            'last_name': ['exact', 'lt', 'lte', 'gte', 'gt'],
        }
