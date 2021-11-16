from django.urls import path,include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from api import views



router= DefaultRouter()
router.register('user', views.UserViewSet, basename='user')
router.register('activiad',views.ActividadViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('inicio/', views.UserLoginApiView.as_view()),

]


