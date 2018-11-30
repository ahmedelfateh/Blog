from django.urls import path
from . import views


# urlpatterns = [

#     # -----------------Post_URLs
#     url(r'^$', views.PostListView.as_view(), name='post_list'),
#     url(r'^about/$', views.AboutView.as_view(), name='about'),
#     url(r'post/(?p<pk>\d+)$', views.PostDetailView.as_view(), name='post_detail'),
#     url(r'post/new/$', views.CreatePostView.as_view(), name='post_new'),
#     url(r'post/(?p<pk>\d+)/edit/$',
#         views.PostUpdateView.as_view(), name='post_edit'),
#     url(r'post/(?p<pk>\d+)/remove/$',
#         views.PostDeleteView.as_view(), name='post_remove'),
#     url(r'^drafts/$', views.DraftListView.as_view(), name='post_new_list'),

#     # -----------------Comment_URLs
#     url(r'post/(?p<pk>\d+)/comment/$',
#         views.add_comment_to_post, name='add_comment_to_post'),
#     url(r'post/(?p<pk>\d+)/approve/$',
#         views.comment_approve, name='comment_approve'),
#     url(r'post/(?p<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
#     url(r'post/(?p<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
# ]

urlpatterns = [

    # -----------------Post_URLs
    path(r'^$', views.PostListView.as_view(), name='post_list'),
    path(r'^about/$', views.AboutView.as_view(), name='about'),
    path(r'post/(?p<pk>\d+)$', views.PostDetailView.as_view(), name='post_detail'),
    path(r'post/new/$', views.CreatePostView.as_view(), name='post_new'),
    path(r'post/(?p<pk>\d+)/edit/$',
         views.PostUpdateView.as_view(), name='post_edit'),
    path(r'post/(?p<pk>\d+)/remove/$',
         views.PostDeleteView.as_view(), name='post_remove'),
    path(r'^drafts/$', views.DraftListView.as_view(), name='post_new_list'),

    # -----------------Comment_URLs
    path(r'post/(?p<pk>\d+)/comment/$',
         views.add_comment_to_post, name='add_comment_to_post'),
    path(r'post/(?p<pk>\d+)/approve/$',
         views.comment_approve, name='comment_approve'),
    path(r'post/(?p<pk>\d+)/remove/$',
         views.comment_remove, name='comment_remove'),
    path(r'post/(?p<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
]
