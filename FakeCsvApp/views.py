from celery.result import AsyncResult
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .tasks import create_csv_task
from .models import Schemas, Columns, DownloadSchemas
from .serializers import (
    SchemaDetailSerializer,
    SchemaListSerializer,
    ColumnDetailSerializer,
    DownloadSchemasListSerializer,
)
from json import loads


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

    def put(self, request, pk):
        try:
            model = Schemas.objects.get(pk=pk)
        except:
            return Response(
                {'message': "Schema was't found!"},
                status=status.HTTP_204_NO_CONTENT
            )

        try:
            instance = SchemaDetailSerializer(model)
            instance.update(
                instance=model,
                validated_data=loads(request.body)
            )
            return Response(
                {'message': "Schema was updated successfully!"},
                status=status.HTTP_302_FOUND
            )
        except:
            return Response(
                {'message': "Schema was't updated!"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class ColumnDetailView(APIView):

    def post(self, request):
        serializer = ColumnDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            Columns.objects.get(pk=pk).delete()
            return Response({
                'message': 'Column was deleted successfully!'},
                status=status.HTTP_204_NO_CONTENT
            )
        except Exception as e:
            Response({
                'message': 'Cannot delete columns'},
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


class DownloadSchemaView(APIView):

    def get(self, request, pk):
        download_schema = DownloadSchemas.objects.get(pk=pk)
        file_name = download_schema.File_name
        response = HttpResponse(
            content_type='text/csv',
            headers={
                'Content-Disposition': f'attachment; filename="media/{file_name}"'},
        )
        return response


class CreateCsvView(APIView):

    def get(self, request, pk, row_num):
        celery_task = create_csv_task.delay(
            schema_id=pk, row_num=row_num
        )
        result = AsyncResult(celery_task.id, app=create_csv_task)
        file_name, date_modified = result.get()
        download_schema = DownloadSchemas.objects.create(
            Schema_id=pk,
            DateModified=date_modified,
            File_name=file_name
        )
        serializer = DownloadSchemasListSerializer(download_schema)
        return Response(serializer.data)
