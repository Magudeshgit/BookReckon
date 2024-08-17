from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import HttpResponse
from . import model



class modelPredict(APIView):
    def get(self, request):
        return Response("Kindly Use POST Method")
    
    def post(self, request):
        value = request.data.get('value')
        print(value)
        resp = model.test(value=value)
        return Response(resp)
    
def empty_resp(request):
    return HttpResponse("This site is managed by Student Research Council of Dr.Mahalingam College of Engineering and Technology, Pollachi - India.")