
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Patil Bank"
admin.site.site_title = "Patil Bank"
admin.site.index_title = "Welcome to Patil Bank"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls'))
]
