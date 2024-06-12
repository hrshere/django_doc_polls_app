from django.urls import path

from . import views
app_name = "polls"
urlpatterns = [
    path("",views.IndexView.as_view(),name="index"),
    #question_id was replaced with pk -to use DetailView instead
    #  of detail() and results(), as it expects primary key value
    #  captured from the url to be called "pk"
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/",views.ResultsView.as_view(),name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote")
]   