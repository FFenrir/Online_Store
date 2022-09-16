from django.contrib import admin
from .models import Product,Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("Name",)

class ProductAdmin(admin.ModelAdmin):
    list_display = ("Name","Manufacturer","Price",)
    list_filter = ("Category",)

admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin)