from django.conf.urls import url

from .views import (
    ResourceList,
    ResourceDetail,
    ResourceCreate,
    ResourceUpdate,
    ResourceDelete,
)

urlpatterns = [

    url(r'^resource/$',
        ResourceList.as_view(),
        name='resourceinfo_resource_list_urlpattern'
        ),

    url(r'^resource/(?P<requested_resource_id>[\d]+)/$',
        ResourceDetail.as_view(),
        name='resourceinfo_resource_detail_urlpattern'
        ),

    url(r'^resource/create/$',
        ResourceCreate.as_view(),
        name='resourceinfo_resource_create_urlpattern'),

    url(r'^resource/(?P<pk>[\d]+)/update/$',
        ResourceUpdate.as_view(),
        name='resourceinfo_resource_update_urlpattern'
        ),

    url(r'^resource/(?P<requested_resource_id>[\d]+)/delete/$',
        ResourceDelete.as_view(),
        name='resourceinfo_resource_delete_urlpattern'
        ),


]
