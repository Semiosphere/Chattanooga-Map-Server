"""View module for handling requests about profiles"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from app_api.models import Profile, ProfilePic
from rest_framework.decorators import action
from django.contrib.auth.models import User

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
    
    @action(methods=['GET'], detail=False)
    def profile(self, request):
        """Get the current user's profile"""
        try:
            profile = Profile.objects.get(user = request.auth.user)
            serializer = ProfileSerializer(profile)
            return Response(serializer.data)
        except User.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'profile_pic', 'locations']
        depth = 1
    
class CreateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'profile_pic']
        