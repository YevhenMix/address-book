from django.conf.urls.static import static
from django.conf import settings
from django.urls import path

from .views import main_view, ResidentCreateView, ResidentUpdateView, resident_delete_view

app_name = 'residents'

urlpatterns = [
    path('', main_view, name='main'),
    path('create/', ResidentCreateView.as_view(), name='create'),
    path('update/<int:pk>', ResidentUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', resident_delete_view, name='delete'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
