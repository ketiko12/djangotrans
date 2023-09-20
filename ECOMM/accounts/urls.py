from django.urls import path
from accounts.views import cart,login_page, register_page, activate_email, remove_cart, remove_coupon, add_to_cart, success

urlpatterns=[
    path('login/', login_page, name='login'),
    path('activate/<email_token>', activate_email, name='activate_email'),
    
    path('register/', register_page, name='register'),
   
    path('cart/', cart, name='cart'),
    path('add_to_cart/<uid>/',add_to_cart, name='add_to_cart'),
    path('remove_cart/<cart_item_uid>/', remove_cart, name='remove_cart'),
    path('remove_coupon/<cart_id>/', remove_coupon, name='remove_coupon'),
    path('success/', success, name='success'),
]