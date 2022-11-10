from django.urls import path
from services import views

urlpatterns = [
    # About ME
    path('all/', views.ServicesApi.as_view(), name="Services")
]
