from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('plc/<int:plc_id>/', views.edit, name='edit'),
]