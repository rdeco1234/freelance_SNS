from django.urls import path

from . import views

app_name = 'app1'

urlpatterns = [
    path('ipaddress/', views.ipaddress, name='ipaddress'),
	path('ipaddress/change/<int:ipaddress_id>/', views.ipaddress_change, name='ipaddress_change'),
]
