from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from .serializers import TreeSerializer
from .models import TreeModel
import sys
sys.path.append("..") # Adds higher directory to python modules path.
from calculator import cfp_output
# Create your views here.

class TreeView(APIView):
    permission_class = [permissions.IsAuthenticated]
    parser_classes = [JSONParser]

    def get(self, request):
        obj = TreeModel.objects.all()
        serializer = TreeSerializer(obj, many=True)
        return Response(serializer.data, status=200)

    def post(self,request):
        request.data['user'] = request.user.id
        obj = TreeSerializer(data=request.data)
        if obj.is_valid():
            obj.save()
            return Response({
                "status":"added",
            }, status=201)
        else:
            return Response({
                "Enter valid tree details."
            }, status=400)

    def delete(self,request, pk):
        try:
            obj = TreeModel.objects.filter(id=pk)
            obj.delete()
            return Response({
                'status': 'deleted'
            },status=200)
        except:
            return Response({
                'Tree does not exist.'
            },status=404)
        
class CarbonFootprintView(APIView):
    permission_class = [permissions.IsAuthenticated]
    parser_classes = [JSONParser]

    def post(self,request):
        output = cfp_output(request.data['food'])
        if not output:
            return Response({
                "Enter a valid food item."
            }, status=400)  
        else:
            return Response(output, status=200)
              