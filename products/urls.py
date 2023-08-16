from django.urls import path

from products.views import products, basket_add, basket_remove

app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
    path('category/<int:category_id>/', products, name='category'), # ../products/category<category_id>
    path('page/<int:page_number>/', products, name='paginator'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),  # ../products/baskets/add/<product_id>
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),  # ../products/baskets/remove/<product_id>
]
