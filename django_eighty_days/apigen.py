import argparse

template = """
class %(name)sList(generics.ListCreateAPIView):
    \"\"\" Create or get %(name)s objects
    
    Without a pk, returns all %(name)s objects.

    With a pk, returns just that %(name)s
    \"\"\"
    queryset = models.%(name)s.objects.all()
    serializer_class = serializers.%(name)sSerializer
"""

parser = argparse.ArgumentParser()
parser.add_argument('names', nargs='+')

opts = parser.parse_args()

for name in opts.names:

    print(template % dict(name=name))

