from django.contrib import admin
from .models import (
    Contributor,
    WorksMetadata
)

admin.site.register(WorksMetadata)
admin.site.register(Contributor)
