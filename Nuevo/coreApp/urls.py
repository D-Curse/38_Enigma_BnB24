from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('filter_people/', views.filter_people, name='filter_people'),
    path('profile/<int:user_id>/',views.profile_view, name='profile_view'),
    path('profile_form/', views.profile_form, name='profile_form'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)