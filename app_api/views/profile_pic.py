"""View module for handling requests about profile pics"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from app_api.models import ProfilePic

class ProfilePicView(ViewSet):
    """Profile Pic View"""
    def list(self, request):
        """Handle GET requests to get all profile pics
        Returns:
            response -- JSON serialized list of profile pics"""
        
        profile_pics = ProfilePic.objects.all()
        serializer = ProfilePicSerializer(profile_pics, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk):
        """Handle GET requests for a single profile pic
        Returns:
            response -- JSON serialized profile pic"""
            
        profile_pic = ProfilePic.objects.get(pk=pk)
        serializer = ProfilePicSerializer(profile_pic, context={'request': request})
        return Response(serializer.data)
        
class ProfilePicSerializer(serializers.ModelSerializer):
    """JSON serializer for the Django profile pic"""
    class Meta:
        model = ProfilePic
        fields = ('id', 'src')