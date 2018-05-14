from django.db import models
from django.core.urlresolvers import reverse


class Resource(models.Model):
    resource_id = models.AutoField(primary_key=True)
    resource_name = models.CharField(max_length=255)
    resource_content = models.CharField(max_length=8000)

    def __str__(self):
        return '%s - %s' % (self.resource_id, self.resource_name)

    def get_absolute_url(self):
        return reverse('resourceinfo_resource_detail_urlpattern',
                       kwargs={'requested_resource_id': self.resource_id}
                       )

    def get_update_url(self):
        return reverse('resourceinfo_resource_update_urlpattern',
                       kwargs={'pk': self.resource_id}
                       )

    def get_delete_url(self):
        return reverse(
            'resourceinfo_resource_delete_urlpattern',
            kwargs={'requested_resource_id': self.resource_id}
        )

    class Meta:
        ordering = ['resource_id']
        permissions = (
            ("view_resource", "Can view resource"),
        )
