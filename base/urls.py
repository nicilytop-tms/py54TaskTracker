from django.contrib import admin
from django.urls import path, include


from base.views import (
    MainPageView, LoginTemplateView
)

urlpatterns = [
    path('', MainPageView.as_view()),
    path('login/', LoginTemplateView.as_view()),
]
