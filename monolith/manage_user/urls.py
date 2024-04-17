from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path('users/', views.UserListView.as_view(), name='list_user'),
]
