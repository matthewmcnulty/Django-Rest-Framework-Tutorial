from django.urls import path

from . import views

# /api/products/
urlpatterns = [
    path('', views.ProductCreateAPIView.as_view()),
    path('<int:pk>/', views.ProductDetailAPIView.as_view())
]