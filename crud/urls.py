from django.contrib import admin
from django.urls import include, path
from api import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('dataapi',views.StudentDataViewSet,basename='dataapi')
router.register('scoreapi',views.StudentScoreViewSet,basename='scoreapi')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework')),
]