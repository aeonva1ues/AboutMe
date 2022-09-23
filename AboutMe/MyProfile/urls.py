from django.urls import path
from django.views.generic import TemplateView
from .views import MyProfileView


urlpatterns = [
    path('', MyProfileView.as_view(template_name="myProfile/main.html")),
]