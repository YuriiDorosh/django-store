from django.contrib import admin

from products.models import ProductCategory, Product, Basket

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'price',
                    'quantity',
                    'categories',
                    )
    fields = ('image',
              'name',
              'description',
              ('price',
               'quantity'
               ),
              'categories',
              )
    search_fields = ('name',
                     )
    ordering = ('name',
                )


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = (
        'product',
        'quantity',
        'created_timestamp',
    )
    readonly_fields = (
        'created_timestamp',
    )
    extra = 0