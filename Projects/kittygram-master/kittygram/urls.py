from django.urls import path

from cats import views

urlpatterns = [
   path('cats/', views.CatList.as_view()),
   path('cats/<int:pk>/', views.CatDetail.as_view()),
]


