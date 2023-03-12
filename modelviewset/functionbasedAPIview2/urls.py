"""functionbasedAPIview2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter() #creating router object
router.register('studentapi',views.StudentModelViewSet,basename='student') #register student viewset with router
routerroeadonly = DefaultRouter()
routerroeadonly.register('readonly',views.StudentReadOnlyModelViewSet,basename='studentreadonly')
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('studentapi/',views.studentapi,name='studentapi'),
    # path('studentapi/<int:pk>',views.studentapi,name='studentapi'),
    # path('StudentAPI/',views.StudentAPI.as_view(),name='StudentAPI'),
    # path('StudentAPI/<int:pk>/',views.StudentAPI.as_view(),name='StudentAPI'),
    # path('studapigen/<int:pk>/',views.StudentRetrieve.as_view(),name='studapigen'),
    # path('studapigen/',views.StudentList.as_view(),name='studapigen'),
    # path('studapigen/<int:pk>/',views.StudentUpdate.as_view(),name='studapigen'),
    # path('studapigen/<int:pk>/',views.StudentDestroy.as_view(),name='studapigen'),
    # path('studapigen/',views.LCStudentListAPI.as_view(),name='studapigen'),
    # path('studapigen/<int:pk>/',views.RUDStudentAPI.as_view(),name='studapigen'),
    # path('studapigen/',views.StudentList.as_view(),name='studapigen'),
    # path('studapigen/',views.StudentCreate.as_view(),name='studapigen'),
    # path('studapigen/<int:pk>/',views.StudentDestroy.as_view(),name='studapigen'),
    # path('studapigen/<int:pk>/',views.StudentRetrieveDestroy.as_view(),name='studapigen'),
    # path('studapigen/',views.StudentListCreate.as_view(),name='studapigen'),
    # path('studapigen/<int:pk>/',views.StudentRetrieveUpdateDestroy.as_view(),name='studapigen'),
    path('',include(router.urls)),
    path('readonlyroot/',include(routerroeadonly.urls)),

]
