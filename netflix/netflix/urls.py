
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from appMy.views import *
from appUser.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',indexPage,name='indexPage'),
    path('netflix',netflix,name='netflix'),
    path('netflix/<catetitle>',netflixType),
    # path('netflixPage<id>',netflixPage,name='netflixPage'),
    # ===USER===
    path('profileUser',profileUser,name='profileUser'),
    path('subscribeUser',subscribeUser,name='subscribeUser'),
    # path('deleteProfileUser<id>',deleteProfileUser,name='deleteProfileUser'),
    path('accountUser',accountUser,name='accountUser'),
    path('loginUser',loginUser,name='loginUser'),
    path('registerUser',registerUser,name='registerUser'),
    path('logout',logoutUser,name='logoutUser'),
    
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
