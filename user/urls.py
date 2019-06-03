from django.conf.urls import url
from user import views

app_name = "user"

urlpatterns = [

    url(r'^user_registration/$',views.user_registration),
    url(r'^link_created/$',views.link_created),
    url(r'^login/$',views.login),
    url(r'^home/$',views.home),
    url(r'^change_password/$',views.change_password),
    url(r'^logout/$',views.logout),



]