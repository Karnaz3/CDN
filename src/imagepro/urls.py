from django.contrib import admin
from django.urls import path,include
from enc_dec import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('enc_dec.urls')),
]
