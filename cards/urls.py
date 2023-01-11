# cards/urls.py

from django.urls import path


from . import views
urlpatterns = [
    path(
        "new",
        views.CardListView.as_view(),
        name="card-create"
    ),
]