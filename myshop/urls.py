from django.urls import re_path, path
from django.contrib.auth import views as auth_views
from . import user_views, views

# app_name="myshop"
urlpatterns = [
    re_path(r'^$', views.index, name = 'index'),
    re_path(r'^brand/(?P<category_name>[\w]+)$', views.brands, name = 'brands'),
    re_path(r'^product/(?P<product_id>[\d]+)$', views.view_product, name='view_product'),
    re_path(r'^add/(?P<product_id>[\d]+)$', views.add_product_to_cart, name='add_product_to_cart'),
    re_path(r'^show-cart$', views.show_cart, name='show_cart'),
    # re_path(r'^change/(?P<action>[a-z]+)/(?P<action>[0-9]+)$', views.add_product_to_cart, name='add_product_to_cart'),
    path("change/<str:action>/<int:product_id>", views.change_product_quantity, name='change_product_quantity'),
    re_path(r'^delete/(?P<product_id>[\d]+)$', views.delete_product_in_cart, name='delete_product_in_cart'),
    re_path(r'^checkout$', views.checkout, name='checkout'),


    re_path(r"^user/register$", user_views.register_user, name='register_user'),
    re_path(r"^user/login$", user_views.login_user, name='login_user'),
    re_path(r"^user/logout$", user_views.logout_user, name='logout_user'),
    re_path(r"^user/validate$", user_views.validate_username, name='validate_username'),
    # re_path(r"^user/change$", user_views.change_password, name='change_password'),
    # re_path(r"^user/validate$", user_views.validate_username, name='validate_username'),

]
