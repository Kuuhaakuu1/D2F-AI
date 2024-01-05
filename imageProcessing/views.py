from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import DataSerializer

class GetDataFromAngular(APIView):
    def get(self, request, *args, **kwargs):
        url = self.request.query_params.get('url', '')
        data = {
            'message': 'Data fetched successfully',
            'url': url,
        }
        print(data)
        print("hello")
        serializer = DataSerializer(data)
        return Response(serializer.data)