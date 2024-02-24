from rest_framework.views import APIView
from rest_framework.response import Response
from ..utils import handle_template_generation


class TemplateGenerateView(APIView):

    def post(self, request):
        handle_template_generation(request.data)
        return Response({"success":True}, status=200)

