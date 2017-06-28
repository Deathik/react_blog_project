from django.conf.urls import url, include

from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.PostList.as_view(), name='index'),
    url(r'^post/new$', views.PostCreate.as_view(), name='post_create'),
    url(r'^post/(?P<pk>\d+)/$', views.PostDetail.as_view(), name='post_detail'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.PostEdit.as_view(), name='post_edit'),
    url(r'^post/(?P<pk>\d+)/delete/$', views.PostDelete.as_view(), name='post_delete'),
    url(r'^login/$', views.Login.as_view(), name='login'),
    url(r'^logout/$', views.Logout.as_view(), name='logout'),
    #url(r'^api/', include('blog.api_v1.urls')),
]
