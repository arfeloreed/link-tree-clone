from django.urls import path

from . import views

# urls path below
urlpatterns = [
    path("", views.IndexView.as_view(), name="home"),
    path("link/create/", views.CreateLinkView.as_view(), name="create-link"),
    path("link/<int:pk>/update/", views.UpdateLinkView.as_view(), name="update-link"),
    path("link/delete/<int:pk>", views.DeleteLinkView.as_view(), name="delete-link"),
    path("<slug:profile_slug>", views.profile, name="profile-view"),
]
