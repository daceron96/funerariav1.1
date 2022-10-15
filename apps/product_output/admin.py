from django.contrib import admin
from .models import ProductOutput, OutputDetail, OutputType

admin.site.register(ProductOutput)
admin.site.register(OutputDetail)
admin.site.register(OutputType)