from django.conf import settings
from rest_framework import serializers

from .models import ShortLink
from .utils import get_random_string


class ShortLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortLink
        fields = ("url", "status_code")


    def create(self, validated_data):
        validated_data["created_by_ip"] = self.context.get("request").META.get(
            "REMOTE_ADDR"
        )
        validated_data["link_id"] = get_random_string(5)
        return ShortLink.objects.create(**validated_data)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["short_url"] = settings.SHORT_BASE_URL + instance.link_id
        return representation


class ShortLinkDetailSerializer(ShortLinkSerializer):
    class Meta:
        model = ShortLink
        fields = "__all__"
