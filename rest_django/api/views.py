from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Person

from api.serializers import PersonSerializer
# Create your views here.

class PersonAPI(APIView):
    def get(self, request, pk = None):
        if pk:
            try:
                person = Person.objects.get(pk=pk)
                serialize = PersonSerializer(person)
                return Response(serialize.data)
            except:
                return Response({'message': 'Person not found'})
        person = Person.objects.all()
        serialize = PersonSerializer(person, many=True)
        return Response(serialize.data)
    
    def post(self, request):
        data = request.data
        serialize = PersonSerializer(data=data)
        if serialize.is_valid():
            serialize.save()
            return Response({'message': 'Person created successfully'})
        return Response(serialize.errors)
    
    def put(self, request, pk = None):
        data = request.data
        person = Person.objects.get(pk=pk)
        serialize = PersonSerializer(person, data=data)
        if serialize.is_valid():
            serialize.save()
            return Response({'message': 'Person updated successfully'})
        return Response(serialize.errors)
    
    def delete(self, request, pk):
        person = Person.objects.get(pk=pk)
        person.delete()
        return Response({'message': 'Person deleted successfully'})