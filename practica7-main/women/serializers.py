from rest_framework import serializers
from .models import Women


class WomenSerializer(serializers.ModelSerializer):
    cat_id = serializers.IntegerField(read_only=True, allow_null=True)

    class Meta:
        model = Women
        fields = ('title', 'cat_id')