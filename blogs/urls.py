from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .feeds import LatestPostsFeed

app_name = 'blogs'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('tag/<slug:tag__slug>/', views.post_list, name='post_list_by_tag'),
    # path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail,
         name='post_detail'),
    path('<int:post_id>/share/',
         views.post_share, name='post_share'),
    path('<int:post_id>/comment/',
         views.post_comment, name='post_comment'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
