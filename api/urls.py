from django.urls import path, include

urlpatterns = [
    path('users/', include('custom_user.urls')),
]
