from django.urls import path
from .views import home, MenuPageView

urlpatterns = [
    path('', home, name="home"),
    path('menu/', MenuPageView.as_view(), name="menu"),
]