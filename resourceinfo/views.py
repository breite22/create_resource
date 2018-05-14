from django.shortcuts import render, get_object_or_404, redirect

from django.views import View
from django.views.generic import ListView, CreateView, UpdateView

from resourceinfo.decorators import require_authenticated_permission
from resourceinfo.forms import ResourceForm
from resourceinfo.utils import PageLinksMixin
from .models import Resource


@require_authenticated_permission(
    'resourceinfo.view_resource')
class ResourceList(PageLinksMixin, ListView):
    paginate_by = 5
    model = Resource


@require_authenticated_permission(
    'resourceinfo.view_resource')
class ResourceDetail(View):

    def get(self, request, requested_resource_id):
        resource = get_object_or_404(
            Resource,
            resource_id=requested_resource_id
        )
        return render(
            request,
            'resourceinfo/resource_detail.html',
	        {'resource': resource,}
         )


@require_authenticated_permission(
    'resourceinfo.add_resource')
class ResourceCreate(CreateView):
    form_class = ResourceForm
    model = Resource


@require_authenticated_permission(
    'resourceinfo.change_resource')
class ResourceUpdate(UpdateView):
    form_class = ResourceForm
    model = Resource
    template_name = 'resourceinfo/resource_form_update.html'


@require_authenticated_permission(
    'resourceinfo.delete_resource')
class ResourceDelete(View):

    def get(self, request, requested_resource_id):
        resource = get_object_or_404(
            Resource,
            resource_id=requested_resource_id
        )
        return render(
            request,
            'resourceinfo/resource_confirm_delete.html',
            {'resource': resource}
            )

    def post(self, request, requested_resource_id):
        resource = get_object_or_404(
            Resource,
            resource_id=requested_resource_id
        )
        resource.delete()
        return redirect('resourceinfo_resource_list_urlpattern')
