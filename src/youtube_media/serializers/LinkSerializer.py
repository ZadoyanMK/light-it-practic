from rest_framework import serializers
from ..models import Links


class LinkSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Links
        # fields = '__all__'
        exclude = ('id', 'updated_at', 'created_at', 'etag')
