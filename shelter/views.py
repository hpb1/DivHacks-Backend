from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from .serializers import ShelterSerializer
from .models import ShelterModel
from geopy.distance import geodesic
# Create your views here.

class ShelterView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [JSONParser]

    def get(self, request):
        obj = ShelterModel.objects.all()
        serializer = ShelterSerializer(obj, many=True)
        return Response(serializer.data, status=200)

    def post(self,request):
        request.data['user'] = request.user.id
        obj = ShelterSerializer(data=request.data)
        if obj.is_valid():
            obj.save()
            return Response({
                "status":"added",
            }, status=201)
        else:
            return Response({
                "Enter valid shelter details."
            }, status=400)
        
    def patch(self, request, pk):
        obj = ShelterModel.objects.get(id=pk)
        serializer = ShelterSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=201)
        else:
            return Response({
                'Shelter does not exist.'
            },status=400)

    def delete(self,request, pk):
        try:
            obj = ShelterModel.objects.filter(id=pk)
            obj.delete()
            return Response({
                'status': 'deleted'
            },status=200)
        except:
            return Response({
                'Shelter does not exist.'
            },status=404)

class NearbyShelters(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [JSONParser]

    def post(self, request):
        user_loc = (request.data['latitude'],request.data['longitude'])
        result = ShelterModel.objects.values()
        res = []
        for i in result:
            shelter_loc = (i['latitude'],i['longitude'])
            if geodesic(user_loc,shelter_loc).miles <= 5:
                res.append(i)
        if not res:
            return Response({
                "No shelters found in a 5 mile radius."
            }, status=200)
        else:
            return Response(res, status=200)
