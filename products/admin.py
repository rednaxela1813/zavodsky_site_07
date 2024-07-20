from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from .models import Address, Phone, Category, Product, Photo, Property, Email


class PhotoInline(GenericTabularInline):
    model = Photo
    extra = 1
    exclude = ['content_type', 'object_id']


class CategoryAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]


class PropertiesInline(GenericTabularInline):
    model = Property
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]
    inlines = [PropertiesInline]




admin.site.register(Category, CategoryAdmin)
admin.site.register(Address)
admin.site.register(Phone)
admin.site.register(Property)
admin.site.register(Product, ProductAdmin)
admin.site.register(Photo)
admin.site.register(Email)
