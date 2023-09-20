from django import admin
from .models import *

admin.site.register(Category)
admin.site.register(Product)


class ProductImageAdmin(admin.StackedInline):
    model=ProductImage
class ProductAdmin(admin.ModelAdmin):
    inlines=[ProductImageAdmin]
    list_display=['product_name','price']
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage) 
@admin.register(ColorVariant) 
class ColorVariantAdmin(admin.ModelAdmin):
    model=ColorVariant
    list_display=['color-name', 'price']
@admin.register(SizeVariant) 
class SizeVariantAdmin(admin.ModelAdmin):
    model=SizeVariant
    list_display=['size-name', 'price']

admin.site.register(Coupon)    



