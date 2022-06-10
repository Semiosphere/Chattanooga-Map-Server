"""View module for handling requests about profile locations"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from app_api.models import ProfileLocation

class ProfileLocationView(ViewSet):
    """Profile Pic View"""
    def list(self, request):
        """Handle GET requests to get all profile locations
        Returns:
            response -- JSON serialized list of profile locations"""
        
        profile_locations = ProfileLocation.objects.all()
        serializer = ProfileLocationSerializer(profile_locations, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk):
        """Handle GET requests for a single profile location
        Returns:
            response -- JSON serialized profile location"""
            
        profile_location = ProfileLocation.objects.get(pk=pk)
        serializer = ProfileLocationSerializer(profile_location, context={'request': request})
        return Response(serializer.data)
        
class ProfileLocationSerializer(serializers.ModelSerializer):
    """JSON serializer for the Django profile location"""
    class Meta:
        model = ProfileLocation
        fields = ('profile', 'location')