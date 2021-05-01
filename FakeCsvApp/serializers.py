from rest_framework import serializers
from .models import Schemas, Columns


class ColumnListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Columns
        exclude = ('Schema', )


class SchemaDetailSerializer(serializers.ModelSerializer):
    column = ColumnListSerializer(many=True)

    class Meta:
        model = Schemas
        fields = '__all__'


class SchemaListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Schemas
        fields = ('id', 'Name',)
