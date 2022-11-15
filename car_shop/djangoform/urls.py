from django.urls import path
from . import views
urlpatterns = [
    path('thanks/', views.thanks,name="thanks"),
    path('review/', views.review,name="review"),
]
