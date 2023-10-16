from django.urls import path
from . import views

app_name='articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/update/', views.update, name='update'),
    
    # 댓글
    path('<int:pk>/comments/', views.create_comment, name='create_comment'),
    path(
        '<int:article_pk>/comments/<int:comment_pk>/',
        views.delete_comment,
        name='delete_comment',
    ),

    # 게시글 좋아요
    path('<int:article_pk>/likes/', views.likes, name='likes'),
]
