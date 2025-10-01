from django.contrib import admin
from django.urls import path,include

#Seria uma espécie de controller

urlpatterns = [
    path('', include('home.urls')),
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
]
