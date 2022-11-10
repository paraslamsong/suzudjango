
from rest_framework import serializers

from projects.models import Projects


class ProjectsSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Projects
        fields = ['name', 'info', 'image', 'link']

    def get_image(self, project):
        request = self.context.get('request')
        image = project.image.url
        return request.build_absolute_uri(image)
