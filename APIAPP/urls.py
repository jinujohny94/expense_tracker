from . import views
from django.urls import path

urlpatterns= [
    path('',views.ActorList.as_view()),
    path('actor/<int:pk>',views.ActorByID.as_view()),
]