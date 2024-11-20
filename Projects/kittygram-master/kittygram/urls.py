from django.urls import path, include
from rest_framework.routers import SimpleRouter
from cats import views


router = SimpleRouter()

router.register('cats', views.CatViewSet)

# urlpatterns = [
#    path('cats/', views.CatList.as_view()),
#    path('cats/<int:pk>/', views.CatDetail.as_view()),
# ]

urlpatterns = [
   path('', include(router.urls))
]


