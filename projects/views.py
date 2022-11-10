from django.http import JsonResponse
from rest_framework.views import APIView

from projects.models import Projects
from projects.serializers import ProjectsSerializer

# Create your views here.


class ProjectsApi(APIView):
    def get(self, request):
        projects = Projects.objects.all().order_by('pk')

        try:
            jsonProjects = ProjectsSerializer(
                projects, many=True,  context={"request": request})
            if not jsonProjects:
                return JsonResponse("data not found", safe=False, status=404)
            return JsonResponse(jsonProjects.data, safe=False)
        except Exception as e:
            return JsonResponse(e, safe=False, status=500)
