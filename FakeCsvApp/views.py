from django.shortcuts import redirect
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
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
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'scheme_list.html'

    def get(self, request):
        schemas = Schemas.objects.filter(User=request.user)
        serializer = SchemaListSerializer(schemas, many=True)
        return Response({'scheme_list': serializer.data})


class SchemaCreateViews(APIView):

    def post(self, request):
        if request.user.is_authentificate():
            schema = Schemas.objects.create(User=request.user)
            serializer = SchemaDetailSerializer(schema)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
