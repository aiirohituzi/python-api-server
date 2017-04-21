"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns
from snippets.views import SnippetViewSet, UserViewSet, api_root  
from rest_framework import renderers

from rest_framework.routers import DefaultRouter


# 라우터를 생성하고 뷰셋을 등록합니다
router = DefaultRouter()  
router.register(r'snippets', views.SnippetViewSet)  
router.register(r'users', views.UserViewSet)


# 이제 API URL을 라우터가 자동으로 인식합니다
# 추가로 탐색 가능한 API를 구현하기 위해 로그인에 사용할 URL은 직접 설정을 했습니다
urlpatterns = [  
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
# DefaultRouter 클래스는 API의 최상단 뷰를 자동으로 생성해주므로, views 모듈에 있는 api_root 메서드와 연결했던 URL도 삭제




# snippet_list = SnippetViewSet.as_view({  
#     'get': 'list',
#     'post': 'create'
# })
# snippet_detail = SnippetViewSet.as_view({  
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# snippet_highlight = SnippetViewSet.as_view({  
#     'get': 'highlight'
# }, renderer_classes=[renderers.StaticHTMLRenderer])
# user_list = UserViewSet.as_view({  
#     'get': 'list'
# })
# user_detail = UserViewSet.as_view({  
#     'get': 'retrieve'
# })

# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url(r'^snippets/$', views.SnippetList.as_view()),
#     url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
#     url(r'^users/$', views.UserList.as_view()),
#     url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    
    # url(r'^$', views.api_root),
    # url(r'^snippets/$',
    #     views.SnippetList.as_view(),
    #     name='snippet-list'),
    # url(r'^snippets/(?P<pk>[0-9]+)/$',
    #     views.SnippetDetail.as_view(),
    #     name='snippet-detail'),
    # url(r'^snippets/(?P<pk>[0-9]+)/highlight/$',
    #     views.SnippetHighlight.as_view(),
    #     name='snippet-highlight'),
    # url(r'^users/$',
    #     views.UserList.as_view(),
    #     name='user-list'),
    # url(r'^users/(?P<pk>[0-9]+)/$',
    #     views.UserDetail.as_view(),
    #     name='user-detail')

#     url(r'^$', api_root),
#     url(r'^snippets/$', snippet_list, name='snippet-list'),
#     url(r'^snippets/(?P<pk>[0-9]+)/$', snippet_detail, name='snippet-detail'),
#     url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', snippet_highlight, name='snippet-highlight'),
#     url(r'^users/$', user_list, name='user-list'),
#     url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail')
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)

# urlpatterns += [  
#     url(r'^api-auth/', include('rest_framework.urls',
#                                namespace='rest_framework')),
# ]