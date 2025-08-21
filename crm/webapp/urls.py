from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name=""),
    path('register', views.register, name="register"),
    path('mylogin', views.my_login, name='mylogin'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('userlogout', views.user_logout, name='userlogout'),
    path('addclient', views.add_client, name='addclient'),
    path('updateclient/<int:pk>', views.update_client, name='updateclient'),
    path('viewclient/<int:pk>', views.view_single_client, name='viewclient'),
    path('deleteclient/<int:pk>', views.delete_client, name='deleteclient'),
]
