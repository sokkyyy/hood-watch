from django.urls import path,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    re_path('^$', views.home, name='home'),
    path('register/',views.register, name='register'),
    path('login/',views.user_login,name='login'),
    path('profile/<int:user_id>/',views.user_profile,name='profile'),
    path('services/<str:hood>/',views.hood_services, name='services'),
    path('hood/posts/<str:hood>/',views.hood_posts,name='services'), 
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)