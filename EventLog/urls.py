from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers

from ev_log import views


router = routers.DefaultRouter()
router.register(r'events', views.EventViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'persons', views.PersonViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include(router.urls))
]
