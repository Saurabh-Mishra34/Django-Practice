from django.urls import path
from . import views



urlpatterns = [
    path("<int:imon>/",views.pracWebmon),
    path("<str:month>/", views.pracWeb)
]