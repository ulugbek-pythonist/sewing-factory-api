from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class HealtCheckView(APIView):
    
    def get(self,request):
        return Response({"message":"Everything is OK, let's go on"},status.HTTP_200_OK)