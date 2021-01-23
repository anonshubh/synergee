from django.urls import path

from . import views

urlpatterns=[
   path('<int:author_id>/<int:category_id>/',views.ListPost.as_view(),name='list-post'),
]