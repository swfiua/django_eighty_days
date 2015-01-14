import inspect
from django.conf import settings

# configure settings
if not settings.configured:
    settings.configure(INSTALLED_APPS=['django_eighty_days'])

from django_eighty_days import models

API_TEMPLATE = """
class %(name)sList(generics.ListCreateAPIView):
    \"\"\" Create or get %(name)s objects
    
    Without a pk, returns all %(name)s objects.

    With a pk, returns just that %(name)s
    \"\"\"
    queryset = models.%(name)s.objects.all()
    serializer_class = serializers.%(name)sSerializer
"""

SERIALIZE_TEMPLATE = """
class %(name)sSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.%(name)s
"""

URL_TEMPLATE = """
    url(r'^%(lname)ss/$', api.%(name)sList.as_view()),
    url(r'^%(lname)ss/(?P<pk>[0-9]+)/$', api.%(name)sList.as_view(), name='%(lname)s-detail'),
"""

def get_models():
    """ Return the model classes for this app

    Return a list of 2-tuples: (name, class)
    """
    items = inspect.getmembers(models, inspect.isclass)

    return [x for x in items if issubclass(x[1], models.models.Model)]

def get_api_code(name):
    """ Generate API class for name """
    return API_TEMPLATE % dict(name=name)

def get_serializer_code(name):
    """ Generate Serializer class for name """
    return SERIALIZE_TEMPLATE % dict(name=name)

def get_url_code(name):
    """ Generate code needed in urls file for name """
    return URL_TEMPLATE % dict(name=name, lname=name.lower())
    

if __name__ == '__main__':

    from cogapp import Cog

    for filename in ('api.py', 'serializers.py', 'urls.py'):
        Cog().main(['cog', '-cr', 'django_eighty_days/' + filename])
