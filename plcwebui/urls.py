from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('ui/', include('ui.urls')),
    path('admin/', admin.site.urls),
]
