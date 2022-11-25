from django.urls import path
from . import views


urlpatterns = [
    path('', views.homePage, name="home"),
    path('room/<str:pk>', views.roomPage, name="room"),
    path('create-room/', views.creatRoom, name="creatroom"),
    path('delete-room/<str:pk>', views.deleteRoom, name="deleteroom"),
    path('login/', views.loginPage, name="loginPage"),
    path('logout/', views.logoutPage, name="logoutPage"),
    path('register/', views.registerPage, name="registerPage"),
    path('profile/', views.profile, name="profile"),
    path("upload-profile/",views.profile_upload,name="uploadprofile"),
    path("upload-post",views.uploadpost,name="uploadPost"),


]
