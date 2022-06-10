"""View module for handling requests about profiles"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from app_api.models import Profile

class ProfileView(ViewSet):
    """Profile View"""
    def update(self, request, pk):
        """Handle PUT requests for a profile

        Returns:
            Response -- Empty body with 204 status code
        """
        profile = Profile.objects.get(pk=pk)
        serializer = CreateProfileSerializer(profile, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class CreateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'profile_pic']