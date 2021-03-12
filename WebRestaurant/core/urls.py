from django.urls import path
from .views import HomePageView, MenuPageView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('menu/', MenuPageView.as_view(), name="menu"),
]