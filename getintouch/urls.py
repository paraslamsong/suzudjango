from django.urls import path
from getintouch import views

urlpatterns = [
    # About ME
    path('send/', views.GetInTouchApi.as_view(), name="Social Media")
]
