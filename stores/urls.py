from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    # path('store', views.create_shop, name='create-store'),
    path('create-store/', views.create_store, name='create-store'),
    path('update-store/<int:s_id>', views.update_store, name='update-store'),
    path('delete-shop/<int:s_id>', views.delete_shop, name='delete-shop'),
    path('view-shops/', views.view_shops, name='view-shop'),

    path('store-profile/<int:s_id>', views.store_profile, name='store-profile'),
    path('upd-store/<int:s_id>', views.upd_store, name = 'upd-store'),
    path('all-stores/', views.all_stores, name="all-stores"),
    path('my-store/', views.my_store, name='my-store'),

    path('store-products/<int:s_id>', views.store_products , name = 'store-products'),

    path('view-products/', views.all_products, name='all-products'),
    path('add-product/<int:s_id>', views.add_product, name='add-product'),
    path('upd-product/<int:p_id>', views.upd_product, name='upd-product'),
    path('delete-product/<int:s_id><int:p_id>', views.delete_product, name='delete-product'),

    path('my-products/', views.my_products, name='my-products'),
    path('my-store-orders/<int:s_id><int:p_id>', views.my_store_orders, name='my-store-orders'),
    path('create-order/<int:s_id>', views.create_order, name='create-order'),

    path('search-stores/', views.search_stores, name='search-stores'),



]
