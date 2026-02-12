from django.urls import path
from .views import home, increment

urlpatterns = [
    path("", home, name="home"),
    path("increment/", increment, name="increment"),
]