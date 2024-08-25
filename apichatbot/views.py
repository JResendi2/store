from openai import OpenAI
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_api_key.models import APIKey
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework import status
from decouple import config
import os
from django.http import JsonResponse
import requests
import json

os.environ['PROJECT_ID'] = config("PROJECT_ID")
os.environ['OPENAI_API_KEY'] = config("KEY_API_OPENAI")
project_id = os.getenv('PROJECT_ID')
api_key = os.getenv('OPENAI_API_KEY')

def cors_exempt(view_func):
    def wrapped_view(request, *args, **kwargs):
        response = view_func(request, *args, **kwargs)
        response["Access-Control-Allow-Origin"] = "*"  
        response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS, DELETE, PUT"
        response["Access-Control-Allow-Headers"] = "Content-Type, X-CSRFToken, authorization"
        return response
    return wrapped_view


class APIChatbot(APIView):
    permission_classes = [HasAPIKey]
    
    @cors_exempt
    def post(self, request):
        if not project_id or not api_key: # Verificar que las variables de entorno están establecidas
            return Response({"status":404, "message": "Las variables de entorno PROJECT_ID o OPENAI_API_KEY no están establecidas."}, status.HTTP_404_NOT_FOUND)
            
        data = request.data
        message = data.get('message')

        client = OpenAI( organization='org-1IYsgOfm9AQRCUV2UlRdbPa6', project= f'{project_id}',)

        url = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        data = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": f"{message} :)"}],
            "temperature": 0.7
        }

        response = requests.post(url, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            return Response({
                "status":200,
                "response": response.json()['choices'][0]['message']['content']
                }, status=status.HTTP_200_OK)
        else:
            return Response({"status":404, "response":response}, status.HTTP_404_NOT_FOUND)


def createCredentials(request):
    api_key, key = APIKey.objects.create_key(name="nombre-correo")
    print("API Key:", key, api_key)
    return JsonResponse({'status':200, 'key': key})