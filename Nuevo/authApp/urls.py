from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('auth/', views.auth_view, name='auth_view'),
    path('user_signup/', views.user_signup, name='user_signup'),
    path('user_login/', views.user_login, name='user_login'),
    path('hr_login/', views.hr_login, name='hr_login'),
    path('admin_section/', views.admin_page, name='admin_page'),
    path('get_hr_uuid/', views.get_hr_uuid, name='get_hr_uuid'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)