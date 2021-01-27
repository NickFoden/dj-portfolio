from django.urls import include, path
from projects import views

urlpatterns = [
    path("", views.all_projects),
    # path("test", views.project_list),
]
