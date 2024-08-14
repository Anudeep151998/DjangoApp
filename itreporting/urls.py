from . import views 
from django.urls import path, include
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

urlpatterns = [ 

    path('', views.home, name = 'home'), 
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('report/', views.report, name='report'),
    path('issue/<int:pk>', PostDetailView.as_view(), name = 'issue-detail'),
    path('issues/', PostListView.as_view(), name='issue-list'),
    path('issue/new', PostCreateView.as_view(), name = 'issue-create'),
    path('issue/<int:pk>/update/', PostUpdateView.as_view(), name = 'issue-update'),
    path('issue/<int:pk>/delete/', PostDeleteView.as_view(), name = 'issue-delete'),
    path('issue/<str:username>', UserPostListView.as_view(), name = 'user-issues'),
]