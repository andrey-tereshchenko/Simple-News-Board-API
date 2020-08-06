from django.urls import path

from news_board_api import views

urlpatterns = [
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('post/create/', views.PostCreateView.as_view(), name='create_post'),
    path('post/detail/<int:pk>/', views.PostDetailView.as_view(),
         name='detail_post'),
    path('posts/', views.PostListView.as_view(), name='posts'),
    path('post/upvote/<int:pk>/', views.PostUpvoteView.as_view(),
         name='upvote_post'),
    path('post/comment/', views.CommentCreateView.as_view(),
         name='create_comment'),
    path('post/<int:pk>/comments/',
         views.CommentListForChosenPostView.as_view(), name='comments'),
    path('post/comment/detail/<int:pk>/', views.CommentDetailView.as_view(),
         name='detail_comment'),
]
