from rest_framework import serializers
from works.models import WorksMetadata


class WorksMetadataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorksMetadata
        fields = ('iswc', 'title', 'contributors')
        depth = 1
