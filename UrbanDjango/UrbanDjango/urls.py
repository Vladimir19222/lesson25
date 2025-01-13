from django.contrib import admin
from django.urls import path
# from task2.views import temp_func, Temp_class
from task4.views import platform_page, games_page, cart_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', platform_page),
    path('platform/games/', games_page),
    path('platform/cart/', cart_page)]
