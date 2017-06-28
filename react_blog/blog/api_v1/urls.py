from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view

from . import views

API_TITLE = 'Blog API'
API_DESCRIPTION = 'This is API for my ReactBlog.'

router = DefaultRouter()
router.register(r'posts', views.PostViewSet)
router.register(r'users', views.UserViewSet)



schema_view = get_schema_view(title='Blog API')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^docs/', include_docs_urls(title=API_TITLE,
                                     description=API_DESCRIPTION)),
    url(r'^schema/$', schema_view),
]
