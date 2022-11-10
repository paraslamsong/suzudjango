from django.http import JsonResponse
from django.shortcuts import render

from getintouch.models import Messages

from rest_framework.views import APIView


# Create your views here.


class GetInTouchApi(APIView):
    def post(self, request):
        print(request.data)
        full_name = request.data['full_name']
        email = request.data['email']
        subject = request.data['subject']
        message = request.data['message']
        try:
            Messages(full_name=full_name, email_address=email, subject=subject,
                     message=message, is_visited=False).save()
            return JsonResponse("Thank you for sending message", safe=False)
        except Exception as e:
            return JsonResponse(e, safe=False, status=500)
