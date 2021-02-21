from django.urls import path
from img_gallery import views
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
    path('gallery/', views.gallery, name = "gallery"),
] + static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)