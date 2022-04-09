
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('', views.exercise_list),
    path('<int:id>', views.exersise_detail),
]

# urlpatterns += staticfiles_urlpatterns