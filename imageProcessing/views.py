from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import DataSerializer
import requests
from rest_framework import status
import json

url = "https://api.faceonlive.com/j2y3q25y1b6maif1/api/iddoc"


class UploadFile(APIView):
    def post(self, request, *args, **kwargs):
        uploaded_file = request.FILES.get('file')

        form = {
            "image": (uploaded_file.name, uploaded_file.file, uploaded_file.content_type),
        }

        headers = {'X-BLOBR-KEY': 'JTJTtDZPvlSktUyI3RomzUv4GQcFG1Zu'}
        response = requests.post(url, files=form, headers=headers)

      

        # Process the file as needed
        # For simplicity, we'll just return a success response
        json_data = json.loads(response.text)
        response_data = {'message': json_data, 'url': 'dummy_url'}

        # Save the response data to a JSON file
        with open('response.json', 'w') as json_file:
            json.dump(json_data, json_file)
        print(response.text)
        serializer = DataSerializer(response_data)
        
        return Response(response_data, status=status.HTTP_200_OK)
