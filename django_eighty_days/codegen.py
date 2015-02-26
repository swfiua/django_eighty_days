import inspect
from django.conf import settings

# configure settings
if not settings.configured:
    settings.configure(INSTALLED_APPS=['django_eighty_days'])

from django_eighty_days import models

API_TEMPLATE = """
class %(name)sFilter(django_filters.FilterSet):
    \"\"\" Filtering %(name)s objects \"\"\"
    class Meta:
        model = models.%(name)s
        fields = %(filter_fields)s

class %(name)sCreate(generics.CreateAPIView):
    \"\"\" Create %(name)s object \"\"\"
    queryset = models.%(name)s.objects.all()
    serializer_class = serializers.%(name)sSerializer

class %(name)sDetail(generics.RetrieveUpdateDestroyAPIView):
    \"\"\" Retrieve, update or delete individual %(name)s objects

    Supply pk of the object to work on.
    \"\"\"
    queryset = models.%(name)s.objects.all()
    serializer_class = serializers.%(name)sSerializer

class %(name)sList(generics.ListCreateAPIView):
    \"\"\" Create or get %(name)s objects

    returns all %(name)s objects.
    \"\"\"
    queryset = models.%(name)s.objects.all()
    serializer_class = serializers.%(name)sSerializer
    filter_class = %(name)sFilter
"""

SERIALIZE_TEMPLATE = """
class %(name)sSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.%(name)s
        depth = %(depth)d
"""

URL_TEMPLATE = """
    url(r'^create_%(lname)s/$', api.%(name)sCreate.as_view(), name='%(lname)s-create'),
    url(r'^detail_%(lname)ss/(?P<pk>[0-9]+)/$', api.%(name)sDetail.as_view(), name='%(lname)s-detail'),
    url(r'^%(lname)ss/$', api.%(name)sList.as_view(), name='%(lname)s-list'),
"""

def get_models():
    """ Return the model classes for this app

    Return a list of 2-tuples: (name, class)
    """
    items = inspect.getmembers(models, inspect.isclass)

    return [x for x in items if issubclass(x[1], models.models.Model)]

def get_api_code(name):
    """ Generate API class for name """
    model = getattr(models, name)
    filter_fields = getattr(model, 'filter_fields', [])
    return API_TEMPLATE % dict(name=name, filter_fields=filter_fields)

def get_serializer_code(name, clazz):
    """ Generate Serializer class for name """
    try:
        depth = clazz.serialize_depth
    except AttributeError:
        depth = 1

    return SERIALIZE_TEMPLATE % dict(name=name, depth=depth)

def get_url_code(name):
    """ Generate code needed in urls file for name """
    return URL_TEMPLATE % dict(name=name, lname=name.lower())
    

if __name__ == '__main__':

    from cogapp import Cog

    for filename in ('api.py', 'serializers.py', 'urls.py'):
        Cog().main(['cog', '-cr', 'django_eighty_days/' + filename])
