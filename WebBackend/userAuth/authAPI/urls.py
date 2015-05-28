from django.conf.urls import url
from authAPI import views
from django.conf.urls import include

urlpatterns = [
	url(r'^user/$', views.UserList.as_view()),
	url(r'^user/(?P<pk>[0-9]+)/$', views.UserInfoDetail.as_view()),
	url(r'^login/',views.Login.as_view()),
	url(r'^logout/',views.Logout),
	url(r'^signup/',views.SignupUser.as_view())
]
#urlpatterns += [
#	url(r'^api-auth/', include('rest_framework.urls',namespace='rest_framework')),
#]
