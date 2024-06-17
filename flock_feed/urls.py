from django.urls import include, path
from django.contrib.auth.decorators import login_required
from .views import homepage, about_page, PostListView, PostDetailView, PostCreateView

urlpatterns = [
    path("", PostListView.as_view(), name="flock_feed_home"),
    path("about/", about_page, name="flock_feed_about"),
    path('post/<uuid:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/create', login_required(PostCreateView.as_view()), name='post_create'),

]
