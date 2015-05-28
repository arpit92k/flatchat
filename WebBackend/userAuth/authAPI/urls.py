from django.conf.urls import url
from authAPI import views
from django.conf.urls import include

urlpatterns = [
	url(r'^user/$', views.UserInfoList.as_view()),
	url(r'^user/(?P<pk>[0-9]+)/$', views.UserInfoDetail.as_view())
]
urlpatterns += [
	url(r'^api-auth/', include('rest_framework.urls',namespace='rest_framework')),
]
