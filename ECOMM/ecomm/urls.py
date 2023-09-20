from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import stettings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns=[
    path('', include('home.urls')),
    path('product/', include('product.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls)
]