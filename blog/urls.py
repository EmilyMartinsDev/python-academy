from django.urls import path, include
from django.conf.urls.static import  static
from django.conf import settings

from . import views
urlpatterns = [
    path("", views.home, name="home"),
    path("posts/<int:post_id>/post_datail", views.post_datail, name='post_datail'),

] + static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)