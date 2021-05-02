from django.contrib import admin
from .models import Columns, Schemas, DownloadSchemas
admin.site.register(Columns)
admin.site.register(Schemas)
admin.site.register(DownloadSchemas)
# Register your models here.
