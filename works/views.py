from django.shortcuts import render
from works.models import WorksMetadata


def single_view(request):
    metadata = WorksMetadata.objects.all().prefetch_related('contributors')
    ctx = {'metadata': metadata}
    return render(request, 'works/single_view.html', ctx)
