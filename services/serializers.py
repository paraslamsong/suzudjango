
from rest_framework import serializers

from services.models import Services


class ServiesSerializer(serializers.ModelSerializer):
    icon = serializers.SerializerMethodField()

    class Meta:
        model = Services
        fields = ['icon', 'title', 'description']

    def get_icon(self, service):
        request = self.context.get('request')
        icon = service.icon.url
        return request.build_absolute_uri(icon)
