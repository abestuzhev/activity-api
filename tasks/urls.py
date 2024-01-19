from django.urls import path

from tasks import views

urlpatterns = [
    path('', views.TaskListView.as_view()),
    path('<int:pk>/', views.TaskDetailView.as_view()),
    path('create/', views.TaskCreateView.as_view()),
    path('update/<int:pk>/', views.TaskUpdateView.as_view()),
    path('delete/<int:pk>/', views.TaskDeleteView.as_view()),
]