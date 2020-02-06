from rest_framework import serializers, viewsets
from .models import Event


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = [
            'id',
            'title',
            'description',
            'created',
            'modified',
            'active',
        ]


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    http_method_names = [
        u'get', u'post', u'put', u'patch', u'delete',
        u'head', u'options', u'trace',
    ]
