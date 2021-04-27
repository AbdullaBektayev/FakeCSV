from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Schemas
from .serializers import SchemaDetailSerializer, SchemaListSerializer


class SchemaDetailViews(APIView):

    def get(self, request, pk):
        schema = Schemas.objects.get(pk=pk)
        serializer = SchemaDetailSerializer(schema)
        return Response(serializer.data)


class SchemaListViews(APIView):

    def get(self, request):
        schemas = Schemas.objects.all()
        serializer = SchemaListSerializer(schemas, many=True)
        return Response(serializer.data)
