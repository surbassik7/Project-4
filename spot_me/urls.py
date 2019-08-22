from django.conf.urls import include, url
from django.views.generic import TemplateView
from rest_framework import routers

from spot_me import views as spot_me_views


router = routers.DefaultRouter()
router.register(r'searches', spot_me_views.SearchViewSet, base_name='searches')


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="spot_me/map.html")),
    url(r'^api/v1/', include(router.urls)),
]
