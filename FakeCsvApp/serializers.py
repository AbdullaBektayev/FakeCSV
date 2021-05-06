from rest_framework import serializers
from .models import Schemas, Columns, DownloadSchemas


class ColumnListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Columns
        exclude = ('Schema', )


class ColumnDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Columns
        fields = '__all__'


class DownloadSchemasListSerializer(serializers.ModelSerializer):

    class Meta:
        model = DownloadSchemas
        fields = '__all__'


class DownloadSchemasDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = DownloadSchemas
        fields = '__all__'


class SchemaDetailSerializer(serializers.ModelSerializer):
    column = ColumnListSerializer(many=True)
    DownloadSchemas = DownloadSchemasListSerializer(many=True)

    class Meta:
        model = Schemas
        fields = '__all__'

    def update(self, instance, validated_data):
        validated_data.pop('DownloadSchemas')
        columns_data = validated_data.pop('column')
        columns = (instance.column).all()
        columns = list(columns)

        instance.Name = validated_data.get('Name', instance.Name)
        instance.Delimiter = validated_data.get(
            'Delimiter',
            instance.Delimiter
        )
        instance.QuoteChar = validated_data.get(
            'QuoteChar',
            instance.QuoteChar
        )
        instance.save()

        for column_data in columns_data:
            if len(columns) > 0:
                column = columns.pop(0)
                column.Name = column_data.get('Name', column.Name)
                column.Type = column_data.get('Type', column.Type)
                column.From = column_data.get('From', column.From)
                column.To = column_data.get('To', column.To)
                column.Order = column_data.get('Order', column.Order)
                column.save()

        return instance


class SchemaListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Schemas
        fields = ('id', 'Name', 'DateModified')
