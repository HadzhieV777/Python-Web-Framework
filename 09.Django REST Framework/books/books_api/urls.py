from django.urls import path
from . import views

urlpatterns = [
    path('', views.BooksListCreate.as_view()),
    path('<int:id>/', views.DetailBookView.as_view()),
]