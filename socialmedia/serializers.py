
from rest_framework import serializers

from socialmedia.models import SocialMedias


class SocialMediasSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = SocialMedias
        fields = ['image', 'name', 'link', 'description']

    def get_image(self, socialmedia):
        request = self.context.get('request')
        image = socialmedia.image.url
        return request.build_absolute_uri(image)
