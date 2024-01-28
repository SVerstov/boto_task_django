from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from .models import ShortLink
from .serializers import ShortLinkSerializer, ShortLinkDetailSerializer
from django.http import HttpResponseRedirect


class ShorLinksApiViewSet(viewsets.ModelViewSet):
    queryset = ShortLink.objects.all().order_by('pk')
    lookup_field = "link_id"

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ShortLinkDetailSerializer
        else:
            return ShortLinkSerializer


def short_link_redirect(request, link_id: str):
    short_link = get_object_or_404(ShortLink, link_id=link_id)
    return HttpResponseRedirect(short_link.url, status=short_link.status_code)
