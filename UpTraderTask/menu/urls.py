from django.urls import path
from django.conf.urls import url
from menu.views import MenuView, MenuViewDetail, MenuApiView


urlpatterns = [
    path('', MenuView.as_view(
        template_name="index.html"
        ),name='menu-item'),
   
    url(r'^(?P<slug>[\w\-]+)/$', 
        MenuViewDetail.as_view(
            template_name="content.html"
            ), name='menu-item'),
    
    path('api/menu/v1/', MenuApiView.as_view(), name='menu_detail')
]