from django.contrib import admin
from django.urls import (
    path,
    include,
)
from works_api.views import single_view_api
from works.views import single_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/metadata/<iswc>', single_view_api),
    path('', single_view),
]
