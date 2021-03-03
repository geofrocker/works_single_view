from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from works.models import WorksMetadata
from .serializers import WorksMetadataSerializer


@api_view(['GET'])
def single_view_api(request, iswc):
    try:
        snippet = WorksMetadata.objects.get(iswc=iswc)
        serializer = WorksMetadataSerializer(snippet)
        return Response(serializer.data)
    except WorksMetadata.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
