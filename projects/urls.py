from django.urls import path
from projects import views

urlpatterns = [
    # About ME
    path('all/', views.ProjectsApi.as_view(), name="Projects")
]
