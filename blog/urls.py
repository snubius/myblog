from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexPage.as_view(), name='index'),
    path('create/', views.CreateBlogView.as_view(), name='create'),
    path('detail/<int:pk>', views.DetailBlogView.as_view(), name='detail'),
    path('update/<int:pk>', views.UpdateBlogView.as_view(), name='update'),
    path('delete/', views.DeleteBlogView.as_view(), name='delete'),
]