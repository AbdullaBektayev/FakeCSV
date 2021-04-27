from rest_framework import serializers
from .models import Schemas, Columns


class ColumnListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Columns
        exclude = ('Schema', 'id')


class SchemaDetailSerializer(serializers.ModelSerializer):
    column = ColumnListSerializer(many=True)

    class Meta:
        model = Schemas
        exclude = ('id',)


class SchemaListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Schemas
        fields = ('id', 'Name',)
