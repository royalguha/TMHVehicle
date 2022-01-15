from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('',views.index,name="login"),
    path('home',views.home,name="index"),
    path("logout",LogoutView.as_view(),name="logout"),
    path("<int:pk>/update",views.DataUpdateView.as_view(),name="update"),
    path("<int:pk>/delete",views.delete,name="delete"),
    path("detail/<int:pk>",views.detail,name="detail"),
]