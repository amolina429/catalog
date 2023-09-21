from django.urls import path, include
# from rest_framework import routers
from .views.products import CreateProductsViews, ListsProductsViews, BrandsViews, UpdateProductsViews, DeleteProductsViews
from .views.query_reports import QueryReportsViews

urlpatterns = [
   #products
   path("products/list/", ListsProductsViews.as_view(), name="get_products"),
   path("products/list/<str:pk>/", ListsProductsViews.as_view(), name="get_product"),
   path("products/create/", CreateProductsViews.as_view(), name="create_products"),
   path("products/update/<int:pk>/", UpdateProductsViews.as_view(), name="update_product"),
   path("products/delete/<int:pk>/", DeleteProductsViews.as_view(), name="update_product"),
   #brands
   path("brands/create/", BrandsViews.as_view(), name="create_brands"),
   #informes
   path("consult/", QueryReportsViews.as_view(), name="get_consult"),
]