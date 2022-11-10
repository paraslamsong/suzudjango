from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView

from aboutme.models import AboutMe, Greetings
from aboutme.serializers import AboutMeSerializer, GreetingSerializer

# Create your views here.


class AboutMeApi(APIView):
    def get(self, request):
        about_mee = AboutMe.objects.all().order_by("-updated_at", '-pk')

        try:
            jsonAboutMee = AboutMeSerializer(
                about_mee, many=True,  context={"request": request})
            if not jsonAboutMee:
                return JsonResponse("data not found", safe=False, status=404)
            return JsonResponse(jsonAboutMee.data[0], safe=False)
        except Exception as e:
            return JsonResponse(e, safe=False, status=500)


class GreetingApi(APIView):
    def get(self, request):
        greetings = Greetings.objects.all().order_by("-updated_at", '-pk')
        try:
            jsonGreetings = GreetingSerializer(
                greetings, many=True,  context={"request": request})
            if not jsonGreetings:
                return JsonResponse("data not found", safe=False, status=404)
            return JsonResponse(jsonGreetings.data[0], safe=False)
        except Exception as e:
            return JsonResponse(e, safe=False, status=500)
