from django.core.serializers import serialize
from django.db.models.query import QuerySet
from django.http import HttpResponse
import json

#from django.utils import simplejson as json


class JsonResponse(HttpResponse):

    def __init__(self, object):
        if isinstance(object, QuerySet):
            content = serialize('json', object)
        else:
            content = json.dumps(
                object, indent=2, cls=json.DjangoJSONEncoder,
                ensure_ascii=False)
        super(JsonResponse, self).__init__(
            content, content_type='application/json')
