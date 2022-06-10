"""View module for handling requests about locations"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from app_api.models import Location, Profile
from rest_framework.decorators import action

class LocationView(ViewSet):
    """Location View"""
    def retrieve(self, request, pk):
        """Handle GET requests for a single location
        Returns:
            response -- JSON serialized location"""
        
        location = Location.objects.get(pk=pk)
        serializer = LocationSerializer(location, context={'request': request})
        return Response(serializer.data)
    
    @action(methods=['post'], detail=True)
    def discover(self, request, pk):
        """Post request for a user to discover a location"""
    
        profile = Profile.objects.get(user=request.auth.user)
        location = Location.objects.get(pk=pk)
        location.discovered_by.add(profile)
        return Response({'message': 'Location discovered!'}, status=status.HTTP_201_CREATED)
    

    
class LocationSerializer(serializers.ModelSerializer):
    """JSON serializer for the Django location"""
    class Meta:
        model = Location
        fields = ('name', 'coordinates', 'description', 'img')
        
        