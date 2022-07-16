from django.contrib import admin
from .models import Category, Product, featureProduct, landing1, activelanding, address, service

#register
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'created']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(landing1)
admin.site.register(activelanding)

admin.site.register(featureProduct)
admin.site.register(address)
admin.site.register(service)
