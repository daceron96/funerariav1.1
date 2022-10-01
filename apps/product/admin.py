from django.contrib import admin
from apps.product.models import Product, ProductCategory, ProductDetail

admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(ProductDetail)