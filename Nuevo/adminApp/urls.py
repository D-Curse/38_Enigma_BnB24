# in urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Your existing patterns
    path('generate_random_data/', views.generate_random_data, name='generate_random_data'),
    path('delete_all_data/', views.delete_all_data, name='delete_all_data'),
    path('display_people/', views.display_people, name='display_people'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)