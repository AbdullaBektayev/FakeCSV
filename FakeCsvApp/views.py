from django.shortcuts import redirect
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Schemas, Columns
from .serializers import SchemaDetailSerializer, SchemaListSerializer


class SchemaDetailViews(APIView):
    def get(self, request, pk):
        schema = Schemas.objects.get(pk=pk)
        serializer = SchemaDetailSerializer(schema)
        return Response(serializer.data)

    def delete(self, request, pk):
        try:
            Schemas.objects.get(pk=pk).delete()
            return Response({'message': 'Tutorial was deleted successfully!'},
                            status=status.HTTP_204_NO_CONTENT
                            )
        except Exception as e:
            schema = Schemas.objects.all()
            serializer = SchemaDetailSerializer(schema)
            return Response(serializer.data)


class ColumnDetailView(APIView):
    def delete(self, request, pk):
        try:
            Columns.objects.get(pk=pk).delete()
            return Response({'message': 'Tutorial was deleted successfully!'},
                            status=status.HTTP_204_NO_CONTENT
                            )
        except Exception as e:
            Response({'message': 'Cannot delete columns'},
                     status=status.HTTP_400_BAD_REQUEST
                     )


class SchemaListViews(APIView):
    def get(self, request):
        schemas = Schemas.objects.all()
        serializer = SchemaListSerializer(schemas, many=True)
        return Response(serializer.data)


class SchemaCreateViews(APIView):

    def post(self, request):
        if request.user.is_authentificate():
            schema = Schemas.objects.create(User=request.user)
            serializer = SchemaDetailSerializer(schema)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
