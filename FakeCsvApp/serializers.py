from rest_framework import serializers
from .models import Schemas, Columns


class ColumnListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Columns
        exclude = ('Schema', )


class ColumnDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Columns
        fields = '__all__'


class SchemaDetailSerializer(serializers.ModelSerializer):
    column = ColumnListSerializer(many=True)

    class Meta:
        model = Schemas
        fields = '__all__'

    def update(self, instance, validated_data):
        columns_data = validated_data.pop('column')
        columns = (instance.column).all()
        columns = list(columns)

        instance.Name = validated_data.get('Name', instance.Name)
        instance.ColumnSeparator = validated_data.get(
            'ColumnSeparator',
            instance.ColumnSeparator
        )
        instance.StringChar = validated_data.get(
            'StringChar',
            instance.StringChar
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
