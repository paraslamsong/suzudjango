
from rest_framework import serializers
from aboutme.models import AboutMe, Greetings


class AboutMeSerializer(serializers.ModelSerializer):
    resume = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()

    class Meta:
        model = AboutMe
        fields = ['about', 'resume', 'image']

    def get_image(self, aboutme):
        request = self.context.get('request')
        image = aboutme.image.url
        return request.build_absolute_uri(image)

    def get_resume(self, aboutme):
        request = self.context.get('request')
        resume = aboutme.resume.url
        return request.build_absolute_uri(resume)


class GreetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Greetings
        fields = ['greet', 'resignation', 'description']
