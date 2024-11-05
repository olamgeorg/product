from django.urls import path
from product.views import *

urlpatterns =[
    path("create", create, name="create"),
    path("edit/<str:id>", edit_product, name="edit"),
    path("delete/<str:id>", delete_product, name="delete"),
    path("shop/<str:id>", shop_product, name="shop"),
]