from django.contrib import admin
from django.urls import path, include

from base.views import (
    MainPageView
)

urlpatterns = [
    path('', MainPageView.as_view())
]
