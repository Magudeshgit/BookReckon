from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from . import modelpredictor

model = modelpredictor()


class modelPredict(APIView):
    def get(self, request):
        return Response("Kindly Use POST Method")
    
    def post(self, request):
        value = request.data.get('value')
        print(value)
        resp = model.test(value=value)
        return Response(resp)