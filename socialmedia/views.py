
from django.http import JsonResponse
from rest_framework.views import APIView

from socialmedia.models import SocialMedias
from socialmedia.serializers import SocialMediasSerializer
# Create your views here.


class SocialMediasApi(APIView):
    def get(self, request):
        socialmedias = SocialMedias.objects.all().order_by('pk')

        try:
            jsonSocialMedias = SocialMediasSerializer(
                socialmedias, many=True,  context={"request": request})
            if not jsonSocialMedias:
                return JsonResponse("data not found", safe=False, status=404)
            return JsonResponse(jsonSocialMedias.data, safe=False)
        except Exception as e:
            return JsonResponse(e, safe=False, status=500)
