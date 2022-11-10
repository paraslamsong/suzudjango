from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView

from services.models import Services
from services.serializers import ServiesSerializer


class ServicesApi(APIView):
    def get(self, request):
        services = Services.objects.all().order_by('pk')
        try:
            jsonServices = ServiesSerializer(
                services, many=True,  context={"request": request})
            print(jsonServices)
            if not jsonServices:
                return JsonResponse("data not found", safe=False, status=404)
            return JsonResponse(jsonServices.data, safe=False)
        except Exception as e:
            return JsonResponse(e, safe=False, status=500)
