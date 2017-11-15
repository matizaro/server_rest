"""serverrest URL Configuration

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
"""
from django.conf.urls import url, include
from rest_framework import routers
from serverrest import views
from django.contrib import admin
from rest_framework.documentation import include_docs_urls, get_schema_view

router = routers.SimpleRouter()

router.register(r'pickups', views.PickupLineViewSet)
router.register(r'ratings', views.PickupLineRatingViewSet)
router.register(r'counted_ratings', views.PickupLineVoteCounterViewSet)
router.register(r'counted_ratings_one_vote/(?P<device_id>[\d\w\-]+)', views.PickupLineDeviceIDViewSet)
router.register(r'device_votes/(?P<device_id>[\d\w\-]+)', views.DeviceIDVotes)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^docs/', include_docs_urls(title='She Is mine api')),
    url(r'^schema/', get_schema_view(title='She Is mine api')),
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
#    url(r'^pickup_lines/$', views.PickupLineViewSet.as_view({'get': 'list'})),
#    url(r'^line_ratings/$', views.PickupLineRatingViewSet.as_view({'get': 'list'})),
#    url(r'^line_ratings_counted/$', views.PickupLineVoteCounterViewSet.as_view({'get': 'list'})),
#    url(r'^device_votes/(?P<deviceid>\d+)/$', views.DeviceIDVotes.as_view({'get': 'list'})),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]