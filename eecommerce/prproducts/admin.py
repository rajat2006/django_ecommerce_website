from django.contrib import admin
from .models import Product,ProductImage
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    date_hierarchy = 'timestamp' #updated
    search_fields = ['title','description']
    list_display = ['title','price', 'active', 'updated']
    list_editable = ['price','active']
    list_filter = ['price', 'active']
    readonly_fields = ['updated', 'active']
    prepopulated_fields = {"slug": ("title",)}
    class Meta:
        model = Product
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
