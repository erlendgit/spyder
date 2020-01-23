from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('app.frontpage.urls')),
    path('admin/', admin.site.urls),
    path('spider/', include('app.spider.urls')),
]
