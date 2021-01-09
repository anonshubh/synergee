from django.urls import path

from . import views


urlpatterns=[
    path('',views.ListProfile.as_view(),name='list-profile'),
    path('profile/<int:id>/',views.DetailProfile.as_view(),name='detail-profile'),
]