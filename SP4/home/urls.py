from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('first/',views.first),
    path('first/random',views.random),
    path('first/logistic',views.logistic),
    path('first/knn',views.knn),
    path('first/tree',views.tree),
    path('predict/result',views.result),
   
]